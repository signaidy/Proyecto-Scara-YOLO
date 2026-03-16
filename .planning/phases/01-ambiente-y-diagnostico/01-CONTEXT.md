# Phase 1: Ambiente y diagnostico base - Context

**Gathered:** 2026-03-16
**Status:** Ready for planning

<domain>
## Phase Boundary

Esta fase cubre solamente la preparacion del ambiente, la verificacion de dependencias y la diagnostica inicial del brick NXT, motores y sensores. No incluye construccion mecanica del SCARA ni entrenamiento de YOLO.

</domain>

<decisions>
## Implementation Decisions

### Runtime and environment
- Python 3 se usara como lenguaje unico de integracion.
- El Dia 1 debe poder ejecutarse tanto en modo `dry-run` como con hardware real.
- El proyecto deja `requirements.txt` y un CLI en `main.py` para evitar pasos manuales ambiguos.

### Hardware diagnostics
- USB es el canal principal hacia el NXT durante desarrollo.
- Los motores se prueban uno por uno con una rutina controlada de giro.
- Los sensores se describen en un perfil JSON editable por puerto y tipo.

### Repository structure
- Se respeta la estructura sugerida por la guia (`vision.py`, `robot.py`, `cinematica.py`, `main.py`, `dataset/`, `modelo/`).
- La evidencia del Dia 1 se documenta en `docs/checklists/day1.md`, `docs/bitacora.md` y `reports/`.

### Claude's Discretion
- Presentacion exacta del reporte Markdown/JSON.
- Mensajes de consola y formato del checklist.

</decisions>

<specifics>
## Specific Ideas

- La rutina del Dia 1 debe servir como smoke test para clases futuras.
- El proyecto debe quedar listo para que un equipo de estudiantes lo pueda seguir en el aula sin buscar scripts adicionales.

</specifics>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Course scope
- `Guia_Proyecto_1_YOLO_SCARA_NXT_9797.docx` - guia docente original con objetivos, restricciones y entregables por dia.
- `docs/specs/guide-summary.md` - resumen operativo de la guia en texto plano.

### Project conventions
- `README.md` - comandos base, estructura del repositorio y foco actual.
- `.planning/REQUIREMENTS.md` - requisitos rastreables por fase.
- `.planning/ROADMAP.md` - definicion de las 6 fases del proyecto.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `main.py`: punto de entrada para diagnosticos del Dia 1.
- `robot.py`: conexion y pruebas del hardware NXT.
- `cinematica.py`: plantilla inicial para D-H.
- `vision.py`: base diferida para YOLO.

### Established Patterns
- CLI con `argparse` y reportes serializables a Markdown/JSON.
- Configuracion de hardware en `config/*.json`.

### Integration Points
- Los resultados del Dia 1 alimentan la seleccion real de puertos y sensores para los Dias 2 y 3.

</code_context>

<deferred>
## Deferred Ideas

- Rutinas de `home` y limites mecanicos - Phase 3.
- Entrenamiento YOLO y parsing de detecciones - Phase 4.
- Calibracion camara-robot y clasificacion completa - Phase 5.

</deferred>

---

*Phase: 01-ambiente-y-diagnostico*
*Context gathered: 2026-03-16*

