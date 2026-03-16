# Proyecto Integrador 1: YOLO + SCARA + LEGO NXT 9797

Este repositorio fue inicializado como proyecto local de Get Shit Done para desarrollar la guia "Deteccion de pelotas rojas y azules con YOLO y clasificacion automatica con brazo robot tipo SCARA basado en LEGO Mindstorms NXT (Kit 9797)".

El foco actual es el Dia 1: preparar el ambiente, verificar dependencias, confirmar la conexion con el NXT y dejar listas las pruebas base de motores y sensores.

## Estado actual

- GSD instalado localmente en `.codex/`
- `.planning/` sembrado con el proyecto, requisitos y roadmap de 6 dias
- CLI de diagnostico para el Dia 1 lista en `main.py`
- Base modular creada para `robot.py`, `vision.py` y `cinematica.py`

## Inicio rapido

Si tu Python de WSL no incluye `venv` o `pip`, usa el Python de Windows:

```bash
python.exe -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/python.exe main.py doctor
./.venv/Scripts/python.exe main.py day1 --dry-run --report reports/day1-dry-run-venv.md --json reports/day1-dry-run-venv.json
```

Si tu Python local si soporta `venv`, el flujo equivalente es:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 main.py doctor
python3 main.py day1 --dry-run --report reports/day1-dry-run.md --json reports/day1-dry-run.json
```

Con el NXT conectado por USB y la configuracion ajustada:

```bash
python3 main.py day1 --config config/hardware.example.json --report reports/day1-live.md --json reports/day1-live.json
```

## Estructura

- `main.py`: CLI para diagnostico de ambiente y Dia 1
- `robot.py`: conexion NXT, verificacion de motores y lectura de sensores
- `vision.py`: base para carga de YOLO e inferencia futura
- `cinematica.py`: utilidades iniciales de cinematica SCARA y tabla D-H
- `config/hardware.example.json`: perfil editable de puertos y sensores
- `docs/checklists/day1.md`: checklist y evidencia requerida del primer dia
- `docs/bitacora.md`: bitacora del proyecto por dia
- `docs/specs/guide-summary.md`: resumen operativo de la guia docente
- `.planning/`: artefactos GSD del proyecto

## Notas de hardware

- La documentacion oficial de NXT-Python recomienda validar la instalacion con `nxt-test`.
- Durante desarrollo, se asume USB como canal principal hacia el NXT.
- `main.py day1 --dry-run` permite verificar estructura y dependencias sin tener el brick conectado.
- En esta maquina el entorno reproducible se creo con `python.exe -m venv .venv` porque el Python de WSL no trae `venv` ni `pip`.
