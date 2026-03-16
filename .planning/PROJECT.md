# Proyecto Integrador 1: YOLO + SCARA + LEGO NXT 9797

## What This Is

Este proyecto de clase integra vision artificial con accion robotica: una webcam detecta pelotas rojas y azules con YOLO, y un brazo tipo SCARA construido con LEGO Mindstorms NXT 9797 las lleva a su zona correspondiente. La implementacion debe quedar modular y reutilizable porque este reto es la base de una serie quincenal de proyectos del curso.

## Core Value

La base del sistema debe quedar utilizable y verificable por etapas para que el equipo pueda conectar deteccion, cinematica y control NXT sin rehacer la arquitectura en cada clase.

## Requirements

### Validated

(None yet - project initialized from course guide)

### Active

- [ ] Dejar el ambiente Python/NXT/YOLO listo y verificable desde la misma laptop de desarrollo.
- [ ] Construir una base modular que separe vision, robotica, cinematica y flujo principal.
- [ ] Cumplir el roadmap de 6 dias con evidencia tecnica diaria y trazabilidad a la guia.

### Out of Scope

- Interfaz grafica avanzada para control del robot - no es necesaria para cumplir los entregables del curso.
- Entrenamiento YOLO multiclase mas alla de `pelota_roja` y `pelota_azul` - agregaria complejidad fuera del alcance del reto.
- Automatizacion cloud o despliegue remoto - el sistema debe ejecutarse localmente en clase junto al NXT.

## Context

La guia docente define una ejecucion 100% presencial en 6 sesiones. Las dependencias centrales son `nxt-python` para el brick LEGO NXT y `ultralytics` para YOLO. La comunicacion recomendada durante desarrollo es por USB y el modelado del robot debe justificarse con parametros Denavit-Hartenberg del prototipo real, no con una tabla generica copiada.

## Constraints

- **Timeline**: 6 sesiones de clase - el avance debe quedar dividido exactamente por dia.
- **Hardware**: LEGO Mindstorms NXT 9797, webcam y baterias - no se asume hardware adicional.
- **Architecture**: Python modular con `vision.py`, `robot.py`, `cinematica.py` y `main.py` - la guia pide base reutilizable.
- **Detection**: YOLO como solucion principal - el color no se resuelve solo con HSV.
- **Kinematics**: Parametros D-H medidos sobre el robot real - la geometria debe coincidir con el SCARA construido.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Instalar GSD local en `.codex/` | Mantener el proyecto alineado con el flujo get-shit-done dentro del repo | ✓ Good |
| Empezar con un CLI de diagnostico para el Dia 1 | La primera necesidad real es verificar ambiente, NXT, motores y sensores | ✓ Good |
| Usar USB como ruta principal para el NXT | Es la recomendacion de la guia y reduce friccion de configuracion | - Pending |
| Mantener modulos Python planos en la raiz | Coincide con la estructura sugerida por la guia y facilita el trabajo en clase | ✓ Good |

---
*Last updated: 2026-03-16 after project initialization from the course guide*
