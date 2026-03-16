# Phase 1 Research: Ambiente y diagnostico base

**Date:** 2026-03-16

## Findings

### NXT-Python

- La instalacion oficial se documenta en `nxt-python` y el flujo de validacion recomendado incluye `nxt-test`.
- La API de localizacion expone `nxt.locator.find(...)` para encontrar y abrir sesion con el brick.
- Los motores pueden operarse desde `brick.get_motor(...)` y `Motor.turn(...)`.
- Los sensores comunes del kit 9797 tienen clases en `nxt.sensor.generic`, incluyendo `Touch`, `Ultrasonic`, `Light` y `Sound`.

### YOLO / Ultralytics

- La instalacion recomendada por la documentacion oficial se hace con el paquete `ultralytics`.
- Para el Dia 1 basta con validar que el paquete exista; entrenamiento e inferencia quedan para la Fase 4.

### Project implications

- Conviene separar el chequeo de dependencias del chequeo de hardware para que el equipo pueda avanzar aunque el NXT no este conectado.
- Un reporte `dry-run` permite preparar la laptop antes de la clase de laboratorio.
- Un perfil JSON por puertos evita hardcodear sensores y facilita ajustar la configuracion real del equipo.

## Decisions reinforced by research

- Mantener USB como flujo principal del Dia 1.
- Implementar `main.py doctor` para dependencias y `main.py day1` para pruebas con el brick.
- Dejar reportes en Markdown/JSON para documentar evidencia y facilitar la bitacora.

