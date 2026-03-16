# Checklist del Dia 1

## Objetivo

Dejar el ambiente listo, confirmar la comunicacion con el brick NXT y documentar el estado real de motores y sensores antes de empezar el montaje SCARA.

## Checklist de ejecucion

- [ ] Crear y activar entorno virtual de Python
- [ ] Instalar dependencias con `python3 -m pip install -r requirements.txt`
- [ ] Ejecutar `python3 main.py doctor`
- [ ] Ejecutar `nxt-test` con el NXT conectado por USB
- [ ] Ejecutar `python3 main.py day1 --config config/hardware.example.json`
- [ ] Verificar motor en puerto A
- [ ] Verificar motor en puerto B
- [ ] Verificar motor en puerto C
- [ ] Leer sensor tactil
- [ ] Leer sensor ultrasonico
- [ ] Registrar bitacora y evidencia del dia

## Evidencia requerida

| Evidencia | Estado | Ruta o nota |
|-----------|--------|-------------|
| Captura de `nxt-test` o equivalente | Pendiente | |
| Video corto de motores en A/B/C | Pendiente | |
| Tabla de sensores verificados | Pendiente | |
| Reporte Markdown de `main.py day1` | Pendiente | `reports/day1-live.md` |
| Reporte JSON de `main.py day1` | Pendiente | `reports/day1-live.json` |

## Tabla de sensores

| Puerto | Sensor esperado | Resultado | Lectura | Observaciones |
|--------|-----------------|-----------|---------|---------------|
| S1 | Touch | Pendiente | | |
| S2 | Ultrasonic | Pendiente | | |
| S3 | Light (opcional) | Pendiente | | |
| S4 | Sound (opcional) | Pendiente | | |

