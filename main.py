"""CLI entrypoint for the YOLO + SCARA + NXT classroom project."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.metadata
import importlib.util
import json
import platform
import sys
from pathlib import Path
from typing import Any

from robot import get_nxt_import_error, load_hardware_profile, run_day1_diagnostics


PACKAGE_CHECKS = (
    {
        "package": "nxt-python",
        "import": "nxt",
        "required": True,
        "purpose": "Control del brick NXT por USB/Bluetooth",
    },
    {
        "package": "ultralytics",
        "import": "ultralytics",
        "required": True,
        "purpose": "Entrenamiento e inferencia de YOLO",
    },
    {
        "package": "opencv-python",
        "import": "cv2",
        "required": False,
        "purpose": "Captura de webcam y video",
    },
    {
        "package": "numpy",
        "import": "numpy",
        "required": False,
        "purpose": "Calculos numericos y matrices",
    },
    {
        "package": "pyusb",
        "import": "usb",
        "required": True,
        "purpose": "Backend USB usado por nxt-python",
    },
)


def build_environment_report() -> dict[str, Any]:
    packages = []
    for check in PACKAGE_CHECKS:
        installed = importlib.util.find_spec(check["import"]) is not None
        version = None
        if installed:
            try:
                version = importlib.metadata.version(check["package"])
            except importlib.metadata.PackageNotFoundError:
                version = "installed"
        packages.append(
            {
                "package": check["package"],
                "import": check["import"],
                "required": check["required"],
                "installed": installed,
                "version": version,
                "purpose": check["purpose"],
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "python": {
            "version": platform.python_version(),
            "executable": sys.executable,
            "platform": platform.platform(),
        },
        "packages": packages,
        "nxt_import_error": get_nxt_import_error(),
    }


def command_doctor(args: argparse.Namespace) -> int:
    report = build_environment_report()
    print(_format_environment_console(report))
    if args.json:
        _write_json(Path(args.json), report)
    return 0


def command_day1(args: argparse.Namespace) -> int:
    profile = load_hardware_profile(args.config)
    environment = build_environment_report()
    hardware = run_day1_diagnostics(profile, dry_run=args.dry_run).to_dict()
    report = {
        "project": "Proyecto Integrador 1 - YOLO + SCARA + NXT 9797",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall_status": _derive_overall_status(environment, hardware),
        "environment": environment,
        "hardware": hardware,
    }

    print(_format_day1_console(report))
    if args.report:
        _write_text(Path(args.report), _format_day1_markdown(report))
    if args.json:
        _write_json(Path(args.json), report)

    if args.dry_run:
        return 0
    return 0 if report["overall_status"] in {"ready", "pending-hardware"} else 1


def _derive_overall_status(environment: dict[str, Any], hardware: dict[str, Any]) -> str:
    required_missing = any(
        item["required"] and not item["installed"] for item in environment["packages"]
    )
    connection_status = hardware["connection"]["status"]
    component_statuses = [entry["status"] for entry in hardware["motors"] + hardware["sensors"]]
    if required_missing:
        return "attention"
    if connection_status == "fail" or "fail" in component_statuses:
        return "attention"
    if hardware["dry_run"] or "skipped" in component_statuses:
        return "pending-hardware"
    return "ready"


def _format_environment_console(report: dict[str, Any]) -> str:
    lines = [
        "Environment doctor",
        f"  Python: {report['python']['version']} ({report['python']['platform']})",
        f"  Executable: {report['python']['executable']}",
        "  Packages:",
    ]
    for item in report["packages"]:
        status = "OK" if item["installed"] else "MISSING"
        version = item["version"] or "-"
        required = "required" if item["required"] else "optional"
        lines.append(
            f"    - {item['package']}: {status} ({required}, version={version})"
        )
    if report["nxt_import_error"]:
        lines.append(f"  nxt import note: {report['nxt_import_error']}")
    return "\n".join(lines)


def _format_day1_console(report: dict[str, Any]) -> str:
    hardware = report["hardware"]
    lines = [
        "Day 1 diagnostic",
        f"  Overall status: {report['overall_status']}",
        f"  Mode: {'dry-run' if hardware['dry_run'] else 'live'}",
        f"  Connection: {hardware['connection']['status']} - {hardware['connection']['details']}",
    ]
    if hardware["brick"]:
        lines.append(
            "  Brick: "
            f"{hardware['brick']['name']} @ {hardware['brick']['address']} "
            f"(free_flash={hardware['brick']['free_flash']})"
        )
    lines.append("  Motors:")
    for motor in hardware["motors"]:
        lines.append(
            f"    - {motor['port']} / {motor['name']}: {motor['status']} - {motor['details']}"
        )
    lines.append("  Sensors:")
    for sensor in hardware["sensors"]:
        sample = sensor["sample"]
        sample_text = "" if sample is None else f" (sample={sample})"
        lines.append(
            f"    - {sensor['port']} / {sensor['name']}: {sensor['status']} - "
            f"{sensor['details']}{sample_text}"
        )
    return "\n".join(lines)


def _format_day1_markdown(report: dict[str, Any]) -> str:
    environment = report["environment"]
    hardware = report["hardware"]
    lines = [
        "# Day 1 Diagnostic Report",
        "",
        f"- Generated: {report['generated_at']}",
        f"- Overall status: `{report['overall_status']}`",
        f"- Mode: `{'dry-run' if hardware['dry_run'] else 'live'}`",
        "",
        "## Environment",
        "",
        "| Package | Required | Installed | Version | Purpose |",
        "|---------|----------|-----------|---------|---------|",
    ]
    for item in environment["packages"]:
        lines.append(
            "| {package} | {required} | {installed} | {version} | {purpose} |".format(
                package=item["package"],
                required="yes" if item["required"] else "no",
                installed="yes" if item["installed"] else "no",
                version=item["version"] or "-",
                purpose=item["purpose"],
            )
        )

    lines.extend(
        [
            "",
            "## Hardware",
            "",
            f"- Connection: `{hardware['connection']['status']}` - {hardware['connection']['details']}",
        ]
    )

    if hardware["brick"]:
        lines.append(
            "- Brick: "
            f"`{hardware['brick']['name']}` @ `{hardware['brick']['address']}` "
            f"(free flash: {hardware['brick']['free_flash']})"
        )

    lines.extend(
        [
            "",
            "### Motors",
            "",
            "| Port | Name | Status | Details |",
            "|------|------|--------|---------|",
        ]
    )
    for motor in hardware["motors"]:
        lines.append(
            f"| {motor['port']} | {motor['name']} | {motor['status']} | {motor['details']} |"
        )

    lines.extend(
        [
            "",
            "### Sensors",
            "",
            "| Port | Name | Status | Sample | Details |",
            "|------|------|--------|--------|---------|",
        ]
    )
    for sensor in hardware["sensors"]:
        sample = "-" if sensor["sample"] is None else sensor["sample"]
        lines.append(
            f"| {sensor['port']} | {sensor['name']} | {sensor['status']} | {sample} | {sensor['details']} |"
        )

    return "\n".join(lines) + "\n"


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Herramientas del Proyecto Integrador 1 (YOLO + SCARA + NXT)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="Revisa Python y dependencias.")
    doctor.add_argument("--json", help="Escribe el reporte de ambiente a JSON.")
    doctor.set_defaults(func=command_doctor)

    day1 = subparsers.add_parser("day1", help="Ejecuta el diagnostico del Dia 1.")
    day1.add_argument(
        "--config",
        default="config/hardware.example.json",
        help="Perfil de puertos y sensores en JSON.",
    )
    day1.add_argument(
        "--dry-run",
        action="store_true",
        help="No intenta conectarse al NXT; solo valida estructura y dependencias.",
    )
    day1.add_argument("--report", help="Escribe el reporte del Dia 1 en Markdown.")
    day1.add_argument("--json", help="Escribe el reporte del Dia 1 en JSON.")
    day1.set_defaults(func=command_day1)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
