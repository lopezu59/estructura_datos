# SmartTaskQueue

Clasificador de tareas por prioridad usando estructuras de datos y reglas de NLP.

## Estructuras de datos:
- Tres colas: Alta, Media y Baja.
- Tareas se encolan según prioridad.

## Funcionalidades:
- `/add-task`: Clasifica y guarda una tarea.
- `/queues`: Muestra el estado actual de todas las colas.
- `/dequeue/<prioridad>`: Elimina la primera tarea de una cola.

## IA utilizada:
- Clasificador de tareas por palabras clave con procesamiento de texto básico.

## Cómo correrlo
1. Instalar dependencias:
```bash
pip install -r requirements.txt
```
2. Ejecutar el servidor:
```bash
python app.py
```
3. Probar endpoints con Postman o curl.

¡Listo para usar! 😄