# Roadmap: Proyecto Integrador 1 - YOLO + SCARA + LEGO NXT 9797

## Overview

El proyecto se ejecuta como una secuencia de 6 fases alineadas con los 6 dias de clase de la guia. Cada fase deja un entregable visible y prepara la siguiente capa: ambiente, mecanica, movimiento, vision, integracion y demostracion final.

## Phases

- [ ] **Phase 1: Ambiente y diagnostico base** - Preparar entorno Python/NXT/YOLO, verificar conexion, motores, sensores y evidencia inicial.
- [ ] **Phase 2: Diseno SCARA y D-H preliminar** - Definir el robot, medir eslabones y fijar una primera tabla D-H.
- [ ] **Phase 3: Robot funcional y movimiento seguro** - Completar montaje, home y validacion de posiciones reproducibles.
- [ ] **Phase 4: Dataset y deteccion YOLO** - Construir dataset, entrenar el modelo y exponer clase/confianza/centroide.
- [ ] **Phase 5: Integracion vision -> coordenadas -> robot** - Mapear camara al espacio de trabajo y ejecutar clasificacion completa.
- [ ] **Phase 6: Ajuste final y demostracion** - Mejorar estabilidad, documentar y presentar el sistema final.

## Phase Details

### Phase 1: Ambiente y diagnostico base
**Goal**: Dejar la computadora, el proyecto y el NXT listos para trabajo repetible en clase.
**Depends on**: Nothing
**Requirements**: ENV-01, ENV-02, ENV-03, NXT-01, NXT-02, NXT-03, DOC-01
**Success Criteria** (what must be TRUE):
  1. El proyecto tiene estructura base, bitacora y artefactos de planning listos.
  2. Existe una rutina reproducible para revisar dependencias y generar reportes del Dia 1.
  3. La conexion al brick y el estado de motores/sensores puede verificarse y documentarse.
**Plans**: 2 plans

Plans:
- [x] 01-01: Crear la base del repositorio, estructura modular y documentacion del Dia 1.
- [x] 01-02: Implementar diagnostico de ambiente, conexion NXT, motores y sensores.

### Phase 2: Diseno SCARA y D-H preliminar
**Goal**: Definir el robot real que se va a construir y su modelo geometrico inicial.
**Depends on**: Phase 1
**Requirements**: ROB-01, KIN-01
**Success Criteria** (what must be TRUE):
  1. El equipo tiene un croquis del SCARA con base, brazo 1, brazo 2 y efector.
  2. Las longitudes reales de eslabones estan medidas y registradas.
  3. Existe una tabla D-H preliminar coherente con el diseno mecanico.
**Plans**: TBD

Plans:
- [ ] 02-01: Documentar configuracion mecanica seleccionada y zona de trabajo.
- [ ] 02-02: Medir robot real y completar tabla D-H preliminar.

### Phase 3: Robot funcional y movimiento seguro
**Goal**: Conseguir movimientos consistentes a posiciones conocidas, con home y limites.
**Depends on**: Phase 2
**Requirements**: NXT-04, KIN-02
**Success Criteria** (what must be TRUE):
  1. El robot puede volver a una posicion home sin choques.
  2. El brazo alcanza el punto de toma y ambas zonas de deposito.
  3. La tabla D-H se corrige con base en el prototipo real.
**Plans**: TBD

Plans:
- [ ] 03-01: Implementar rutinas manuales, home y limites.
- [ ] 03-02: Validar alcance, ajustar holguras y actualizar D-H.

### Phase 4: Dataset y deteccion YOLO
**Goal**: Tener un detector confiable para `pelota_roja` y `pelota_azul`.
**Depends on**: Phase 3
**Requirements**: VIS-01, VIS-02
**Success Criteria** (what must be TRUE):
  1. El dataset fue capturado y etiquetado en el entorno real de clase.
  2. El modelo distingue rojo y azul con evidencia visible.
  3. El codigo devuelve clase, confianza y posicion util del objeto detectado.
**Plans**: TBD

Plans:
- [ ] 04-01: Capturar y etiquetar dataset.
- [ ] 04-02: Entrenar, validar e integrar inferencia base en `vision.py`.

### Phase 5: Integracion vision -> coordenadas -> robot
**Goal**: Convertir la deteccion en un movimiento completo de clasificacion.
**Depends on**: Phase 4
**Requirements**: INT-01, INT-02
**Success Criteria** (what must be TRUE):
  1. Existe una calibracion reproducible entre pixeles y espacio de trabajo.
  2. El sistema decide la zona de destino a partir del color detectado.
  3. El robot ejecuta la secuencia de clasificacion sin intervencion manual durante la prueba.
**Plans**: TBD

Plans:
- [ ] 05-01: Calibrar camara y conversion de coordenadas.
- [ ] 05-02: Integrar deteccion, decision, cinematica y comandos NXT.

### Phase 6: Ajuste final y demostracion
**Goal**: Mejorar robustez, cerrar la documentacion y preparar la defensa tecnica.
**Depends on**: Phase 5
**Requirements**: DOC-01
**Success Criteria** (what must be TRUE):
  1. El sistema corre de forma estable durante la demostracion final.
  2. El equipo puede explicar arquitectura, D-H, deteccion y control NXT.
  3. Codigo, bitacora y evidencia quedan organizados para reutilizarse en el siguiente reto.
**Plans**: TBD

Plans:
- [ ] 06-01: Afinar estabilidad y tiempos de ejecucion.
- [ ] 06-02: Consolidar documentacion y guion de demostracion.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5 -> 6

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Ambiente y diagnostico base | 2/2 | Complete | 2026-03-16 |
| 2. Diseno SCARA y D-H preliminar | 0/2 | Not started | - |
| 3. Robot funcional y movimiento seguro | 0/2 | Not started | - |
| 4. Dataset y deteccion YOLO | 0/2 | Not started | - |
| 5. Integracion vision -> coordenadas -> robot | 0/2 | Not started | - |
| 6. Ajuste final y demostracion | 0/2 | Not started | - |
