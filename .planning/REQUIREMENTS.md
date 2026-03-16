# Requirements: Proyecto Integrador 1 - YOLO + SCARA + LEGO NXT 9797

**Defined:** 2026-03-16
**Core Value:** La base del sistema debe quedar utilizable y verificable por etapas para que el equipo pueda conectar deteccion, cinematica y control NXT sin rehacer la arquitectura en cada clase.

## v1 Requirements

### Environment and Foundation

- [ ] **ENV-01**: El repositorio contiene la estructura base sugerida por la guia (`dataset/`, `modelo/`, `vision.py`, `robot.py`, `cinematica.py`, `main.py`, bitacora y planning).
- [ ] **ENV-02**: El equipo puede verificar desde Python si las dependencias de YOLO y NXT estan instaladas correctamente.
- [ ] **ENV-03**: El proyecto genera un reporte del Dia 1 reutilizable en formato Markdown o JSON.

### NXT Diagnostics

- [ ] **NXT-01**: La laptop puede establecer conexion con el brick NXT por USB.
- [ ] **NXT-02**: Los motores en A, B y C pueden probarse individualmente con una rutina controlada.
- [ ] **NXT-03**: Los sensores configurados en el perfil pueden leerse y dejar evidencia del puerto que funciona.
- [ ] **NXT-04**: El robot dispone de rutina `home` y movimientos seguros para pruebas repetibles.

### Robot and Kinematics

- [ ] **ROB-01**: El equipo define un SCARA didactico con medidas reales y volumen de trabajo alcanzable.
- [ ] **KIN-01**: El proyecto almacena una plantilla D-H y utilidades geometricas que puedan completarse con medidas reales.
- [ ] **KIN-02**: La tabla D-H final coincide con el robot construido y con el codigo de movimiento.

### Vision

- [ ] **VIS-01**: El sistema reconoce las clases `pelota_roja` y `pelota_azul` con evidencia de entrenamiento o validacion.
- [ ] **VIS-02**: La deteccion expone clase, confianza y posicion del objeto para integracion posterior.

### Integration and Evidence

- [ ] **INT-01**: La salida de vision puede convertirse a coordenadas utiles para el area de trabajo del SCARA.
- [ ] **INT-02**: El sistema completo decide destino por color y ejecuta la secuencia de clasificacion.
- [ ] **DOC-01**: La bitacora diaria documenta actividades, fallos y siguiente accion por cada dia del roadmap.

## v2 Requirements

### Future Improvements

- **V2-01**: Agregar realimentacion con sensores para confirmar toma o deposito.
- **V2-02**: Exportar el modelo YOLO a un formato optimizado para inferencia mas rapida.
- **V2-03**: Automatizar calibracion camara-robot con marcas o tablero de referencia.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Clasificacion de mas de dos colores | No esta en la guia del proyecto 1 |
| Desarrollo de una app movil o dashboard web | No aporta al objetivo evaluado en clase |
| Navegacion autonoma del robot fuera de la mesa | El reto es de manipulacion puntual, no de movilidad |
| Bluetooth como flujo principal de desarrollo | USB es mas simple y estable para el laboratorio |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| ENV-01 | Phase 1 | Complete |
| ENV-02 | Phase 1 | Complete |
| ENV-03 | Phase 1 | Complete |
| NXT-01 | Phase 1 | Complete |
| NXT-02 | Phase 1 | Complete |
| NXT-03 | Phase 1 | Complete |
| DOC-01 | Phase 1 | In Progress |
| ROB-01 | Phase 2 | Pending |
| KIN-01 | Phase 2 | In Progress |
| NXT-04 | Phase 3 | Pending |
| KIN-02 | Phase 3 | Pending |
| VIS-01 | Phase 4 | Pending |
| VIS-02 | Phase 4 | Pending |
| INT-01 | Phase 5 | Pending |
| INT-02 | Phase 5 | Pending |

**Coverage:**
- v1 requirements: 15 total
- Mapped to phases: 15
- Unmapped: 0

---
*Requirements defined: 2026-03-16*
*Last updated: 2026-03-16 after live Day 1 diagnostics and phase transition*
