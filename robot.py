"""NXT helpers for classroom diagnostics and later robot control."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any

try:
    import nxt.backend.usb as nxt_usb_backend
    import nxt.locator as nxt_locator
    import nxt.motor as nxt_motor
    import nxt.sensor as nxt_sensor
    import nxt.sensor.generic as nxt_sensor_generic
except Exception as exc:  # pragma: no cover - depends on local hardware libs
    nxt_usb_backend = None
    nxt_locator = None
    nxt_motor = None
    nxt_sensor = None
    nxt_sensor_generic = None
    NXT_IMPORT_ERROR = exc
else:
    NXT_IMPORT_ERROR = None

try:
    import usb.core as pyusb_core
except Exception:  # pragma: no cover - depends on local hardware libs
    pyusb_core = None

try:
    import libusb_package
except Exception:  # pragma: no cover - optional on non-Windows hosts
    libusb_package = None


VALID_MOTOR_PORTS = {"A", "B", "C"}
VALID_SENSOR_PORTS = {"S1", "S2", "S3", "S4"}
SUPPORTED_SENSOR_TYPES = {"auto", "touch", "ultrasonic", "light", "sound"}


@dataclass
class DiagnosticEntry:
    name: str
    port: str
    status: str
    details: str
    sample: Any | None = None


@dataclass
class Day1HardwareReport:
    generated_at: str
    dry_run: bool
    connection: DiagnosticEntry
    brick: dict[str, Any] | None = None
    motors: list[DiagnosticEntry] = field(default_factory=list)
    sensors: list[DiagnosticEntry] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "generated_at": self.generated_at,
            "dry_run": self.dry_run,
            "connection": asdict(self.connection),
            "brick": self.brick,
            "motors": [asdict(entry) for entry in self.motors],
            "sensors": [asdict(entry) for entry in self.sensors],
        }


def load_hardware_profile(path: str | Path) -> dict[str, Any]:
    """Load and minimally validate the classroom hardware profile."""

    profile_path = Path(path)
    raw = json.loads(profile_path.read_text(encoding="utf-8"))
    profile = {
        "brick": raw.get("brick", {}),
        "motors": raw.get("motors", []),
        "sensors": raw.get("sensors", []),
    }

    for motor in profile["motors"]:
        port = str(motor.get("port", "")).upper()
        if port not in VALID_MOTOR_PORTS:
            raise ValueError(f"Unsupported motor port: {port}")

    for sensor in profile["sensors"]:
        port = str(sensor.get("port", "")).upper()
        sensor_type = str(sensor.get("type", "auto")).lower()
        if port not in VALID_SENSOR_PORTS:
            raise ValueError(f"Unsupported sensor port: {port}")
        if sensor_type not in SUPPORTED_SENSOR_TYPES:
            raise ValueError(
                f"Unsupported sensor type '{sensor_type}' on port {port}"
            )

    return profile


def nxt_available() -> bool:
    return all(module is not None for module in (nxt_locator, nxt_motor, nxt_sensor))


def get_nxt_import_error() -> str | None:
    if NXT_IMPORT_ERROR is None:
        return None
    return repr(NXT_IMPORT_ERROR)


def run_day1_diagnostics(
    profile: dict[str, Any],
    *,
    dry_run: bool = False,
) -> Day1HardwareReport:
    """Run Day 1 connectivity, motor and sensor checks."""

    report = Day1HardwareReport(
        generated_at=datetime.now(timezone.utc).isoformat(),
        dry_run=dry_run,
        connection=DiagnosticEntry(
            name="NXT connection",
            port="-",
            status="skipped" if dry_run else "pending",
            details="Dry-run mode selected." if dry_run else "Waiting for connection.",
        ),
    )

    if dry_run:
        report.motors = [_dry_run_motor_entry(motor) for motor in profile["motors"]]
        report.sensors = [_dry_run_sensor_entry(sensor) for sensor in profile["sensors"]]
        return report

    if not nxt_available():
        report.connection = DiagnosticEntry(
            name="NXT connection",
            port="-",
            status="fail",
            details=(
                "nxt-python is not importable. Install requirements and confirm libusb/"
                f"PyUSB support. Import error: {get_nxt_import_error()}"
            ),
        )
        return report

    connect_filters = {
        key: value
        for key, value in profile.get("brick", {}).items()
        if value not in (None, "", [])
    }
    locator_kwargs = dict(connect_filters)
    usb_backend = _get_windows_usb_backend()
    if usb_backend is not None:
        locator_kwargs["backends"] = [usb_backend]
        locator_kwargs["config"] = None

    try:
        with nxt_locator.find(**locator_kwargs) as brick:
            report.connection = DiagnosticEntry(
                name="NXT connection",
                port="-",
                status="pass",
                details="Brick encontrado y sesion abierta.",
            )
            report.brick = _get_brick_info(brick)
            report.motors = [_test_motor(brick, motor) for motor in profile["motors"]]
            report.sensors = [
                _test_sensor(brick, sensor) for sensor in profile["sensors"]
            ]
    except Exception as exc:  # pragma: no cover - requires hardware
        report.connection = DiagnosticEntry(
            name="NXT connection",
            port="-",
            status="fail",
            details=_format_connection_error(exc, connect_filters, usb_backend is not None),
        )

    return report


def _get_windows_usb_backend() -> Any | None:
    """Use libusb-package automatically on Windows when available."""

    if os.name != "nt":
        return None
    if libusb_package is None or nxt_usb_backend is None or pyusb_core is None:
        return None

    backend = libusb_package.get_libusb1_backend()
    if backend is None:
        return None

    class _LibUSBPackageUSBBackend:
        def find(self, **kwargs: Any) -> Any:
            for dev in pyusb_core.find(
                find_all=True,
                idVendor=nxt_usb_backend.ID_VENDOR_LEGO,
                idProduct=nxt_usb_backend.ID_PRODUCT_NXT,
                backend=backend,
            ) or []:
                sock = nxt_usb_backend.USBSock(dev)
                brick = sock.connect()
                yield brick

    return _LibUSBPackageUSBBackend()


def _format_connection_error(
    exc: Exception,
    connect_filters: dict[str, Any],
    using_windows_usb_backend: bool,
) -> str:
    exc_name = exc.__class__.__name__

    if exc_name == "NoBackendError":
        return (
            "PyUSB no encontro un backend USB disponible. Instala y usa libusb en "
            "Windows o verifica el backend nativo de libusb/PyUSB. "
            f"Error original: {exc}"
        )

    if exc_name == "BrickNotFoundError":
        if using_windows_usb_backend:
            filter_note = (
                f" Filtros activos: {connect_filters}."
                if connect_filters
                else ""
            )
            return (
                "No se encontro un brick NXT por USB. El backend libusb esta cargado, "
                "pero Windows no esta exponiendo un dispositivo LEGO NXT al backend USB."
                " Verifica que el brick este encendido, que el cable USB sea de datos, "
                "prueba otro puerto y confirma en Windows un dispositivo con "
                "VID_0694/PID_0002. Si aparece un dispositivo LEGO/NXT, instala un "
                "driver WinUSB o libusbK para ese dispositivo." + filter_note
            )
        return f"No se encontro ningun brick que coincida con los filtros: {connect_filters or 'sin filtros'}."

    return f"No fue posible conectar con el brick: {exc}"


def _dry_run_motor_entry(motor: dict[str, Any]) -> DiagnosticEntry:
    port = str(motor["port"]).upper()
    label = motor.get("label", f"motor_{port.lower()}")
    return DiagnosticEntry(
        name=label,
        port=port,
        status="skipped",
        details="Pendiente de prueba fisica en el NXT.",
    )


def _dry_run_sensor_entry(sensor: dict[str, Any]) -> DiagnosticEntry:
    port = str(sensor["port"]).upper()
    label = sensor.get("label", f"sensor_{port.lower()}")
    return DiagnosticEntry(
        name=label,
        port=port,
        status="skipped",
        details="Pendiente de lectura fisica del sensor.",
        sample=None,
    )


def _get_brick_info(brick: Any) -> dict[str, Any]:
    name, address, signal_strength, free_flash = brick.get_device_info()
    return {
        "name": name,
        "address": address,
        "signal_strength": list(signal_strength),
        "free_flash": free_flash,
    }


def _test_motor(brick: Any, motor_spec: dict[str, Any]) -> DiagnosticEntry:
    port_name = str(motor_spec["port"]).upper()
    label = motor_spec.get("label", f"motor_{port_name.lower()}")

    if not motor_spec.get("enabled", True):
        return DiagnosticEntry(
            name=label,
            port=port_name,
            status="skipped",
            details="Motor marcado como deshabilitado en el perfil.",
        )

    port = getattr(nxt_motor.Port, port_name)
    motor = brick.get_motor(port)
    power = int(motor_spec.get("power", 80))
    degrees = int(motor_spec.get("degrees", 120))
    timeout = int(motor_spec.get("timeout", 2))

    try:
        motor.turn(power, degrees, timeout=timeout)
        return DiagnosticEntry(
            name=label,
            port=port_name,
            status="pass",
            details=f"Giro ejecutado: {degrees} grados a potencia {power}.",
        )
    except Exception as exc:  # pragma: no cover - requires hardware
        return DiagnosticEntry(
            name=label,
            port=port_name,
            status="fail",
            details=f"Fallo al mover el motor: {exc}",
        )
    finally:
        try:
            motor.idle()
        except Exception:
            pass


def _test_sensor(brick: Any, sensor_spec: dict[str, Any]) -> DiagnosticEntry:
    port_name = str(sensor_spec["port"]).upper()
    label = sensor_spec.get("label", f"sensor_{port_name.lower()}")
    sensor_type = str(sensor_spec.get("type", "auto")).lower()

    if not sensor_spec.get("enabled", True):
        return DiagnosticEntry(
            name=label,
            port=port_name,
            status="skipped",
            details="Sensor marcado como deshabilitado en el perfil.",
        )

    port = getattr(nxt_sensor.Port, port_name)

    try:
        sensor = _build_sensor(brick, port, sensor_type)
        sample = sensor.get_sample()
        return DiagnosticEntry(
            name=label,
            port=port_name,
            status="pass",
            details=f"Lectura obtenida para sensor {sensor_type}.",
            sample=sample,
        )
    except Exception as exc:  # pragma: no cover - requires hardware
        return DiagnosticEntry(
            name=label,
            port=port_name,
            status="fail",
            details=f"No fue posible leer el sensor {sensor_type}: {exc}",
        )


def _build_sensor(brick: Any, port: Any, sensor_type: str) -> Any:
    if sensor_type == "auto":
        return brick.get_sensor(port)
    if sensor_type == "touch":
        return brick.get_sensor(port, nxt_sensor_generic.Touch)
    if sensor_type == "ultrasonic":
        return brick.get_sensor(port, nxt_sensor_generic.Ultrasonic)
    if sensor_type == "light":
        return brick.get_sensor(port, nxt_sensor_generic.Light)
    if sensor_type == "sound":
        return brick.get_sensor(port, nxt_sensor_generic.Sound)
    raise ValueError(f"Unsupported sensor type: {sensor_type}")
