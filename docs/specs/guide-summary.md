# Resumen operativo de la guia

## Objetivo del proyecto

Construir en 6 sesiones de clase un sistema que detecte pelotas rojas y azules con YOLO y las clasifique con un brazo robot tipo SCARA basado en LEGO Mindstorms NXT 9797, usando Python como capa de integracion y una tabla Denavit-Hartenberg propia del robot real.

## Restricciones relevantes

- Trabajo 100% presencial y ejecutado solo en clase.
- Plataforma base: LEGO Mindstorms Education NXT 9797.
- Insumos externos permitidos: webcam y baterias.
- La deteccion principal debe usar YOLO, no solo umbralizacion de color.
- El modelado mecanico debe justificarse con parametros D-H medidos en el robot real.
- La comunicacion recomendada con el NXT durante desarrollo es por USB.

## Desglose por dia

### Dia 1

- Verificar Python y dependencias.
- Instalar Ultralytics YOLO y NXT-Python.
- Probar conexion con el NXT.
- Verificar motores en puertos A, B y C.
- Probar sensores disponibles, en especial tactil y ultrasonico.
- Definir repositorio y bitacora.

Entregable: checklist de instalacion, captura o evidencia equivalente de `nxt-test`, video corto de motores y tabla de sensores verificados.

### Dia 2

- Disenar el SCARA.
- Medir eslabones.
- Definir marcos y tabla D-H preliminar.
- Ubicar las zonas roja y azul.

### Dia 3

- Completar montaje.
- Implementar home y movimientos seguros.
- Validar alcance y actualizar tabla D-H.

### Dia 4

- Capturar y etiquetar dataset.
- Entrenar YOLO para `pelota_roja` y `pelota_azul`.
- Validar inferencia y extraer centroide, clase y confianza.

### Dia 5

- Calibrar camara y area de trabajo.
- Conectar deteccion, decision, cinematica y comandos NXT.
- Ejecutar clasificacion completa en pruebas controladas.

### Dia 6

- Ajuste fino.
- Demostracion final.
- Entrega de codigo organizado y bitacora final.

## Base de codigo sugerida por la guia

- `dataset/`
- `modelo/`
- `vision.py`
- `robot.py`
- `cinematica.py`
- `main.py`
- `bitacora` en documento o PDF

