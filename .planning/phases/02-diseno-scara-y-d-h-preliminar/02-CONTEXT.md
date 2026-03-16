# Phase 2: Diseno SCARA y D-H preliminar - Context

**Gathered:** 2026-03-16
**Status:** Ready for planning

<domain>
## Phase Boundary

Esta fase define la configuracion mecanica del SCARA didactico, mide eslabones reales y produce una tabla D-H preliminar coherente con el robot que el equipo va a construir. No incluye todavia rutinas de movimiento reproducible ni integracion con YOLO.

</domain>

<decisions>
## Implementation Decisions

### Mechanical scope
- El robot seguira la recomendacion de la guia: SCARA didactico con 3 GDL usando los tres motores del kit 9797.
- La base, brazo 1, brazo 2 y efector final deben mantenerse compactos y ligeros para minimizar bloqueos mecanicos.
- Las zonas roja y azul deben ubicarse dentro del alcance real del prototipo.

### Kinematics scope
- La tabla D-H debe construirse con medidas tomadas del robot real, no con valores genericos.
- `cinematica.py` ya ofrece una plantilla base; en esta fase debe llenarse con dimensiones reales y marcos definidos por el equipo.
- El resultado esperado es una tabla D-H preliminar y un croquis medido, no una cinematica final validada.

### Hardware carry-forward
- La conexion USB al brick ya esta validada.
- Los motores A/B/C reportaron `Blocked!` en el diagnostico del Dia 1; Phase 2 debe considerar fricciones, topes o montaje antes de avanzar a Phase 3.
- El tactil S1 funciona; el ultrasonico S2 requiere revision adicional.

### Claude's Discretion
- Formato exacto del croquis y de la tabla D-H preliminar.
- Organizacion de documentos auxiliares para medidas y zonas de deposito.

</decisions>

<specifics>
## Specific Ideas

- Priorizar una geometria alcanzable y estable sobre una extension maxima del brazo.
- Usar el tactil S1 como candidato a homing cuando se planifique Phase 3.

</specifics>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Course scope
- `Guia_Proyecto_1_YOLO_SCARA_NXT_9797.docx` - guia docente original.
- `docs/specs/guide-summary.md` - resumen operativo de la guia.

### Current project state
- `.planning/ROADMAP.md` - define el objetivo y criterios de Phase 2.
- `.planning/phases/01-ambiente-y-diagnostico/01-VERIFICATION.md` - hallazgos live del hardware a considerar en el diseno.
- `cinematica.py` - plantilla inicial para la tabla D-H y la cinematica plana.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `cinematica.py`: plantilla D-H y cinematica plana base.
- `reports/day1-live-pythonexe.json`: evidencia real del estado de motores y sensores.
- `config/hardware.example.json`: puertos actuales del hardware.

### Established Patterns
- Evidencia tecnica almacenada en `reports/`.
- Planning por fase dentro de `.planning/phases/`.

### Integration Points
- Las medidas del robot real alimentaran `cinematica.py`.
- La seleccion mecanica condicionara las rutinas de movimiento de Phase 3.

</code_context>

<deferred>
## Deferred Ideas

- Implementacion de `home` y limites mecanicos - Phase 3.
- Dataset y entrenamiento YOLO - Phase 4.
- Integracion vision-robot - Phase 5.

</deferred>

---

*Phase: 02-diseno-scara-y-d-h-preliminar*
*Context gathered: 2026-03-16*
