# SmartTaskQueue

Clasificador de tareas por prioridad usando estructuras de datos y reglas de NLP.

## Estructuras de datos:
- Tres colas: Alta, Media y Baja.
- Tareas se encolan según prioridad.

## Funcionalidades:
- `/`: Te lleva al archivo principal y vizualizar tus tareas
- `/add-task`: Clasifica y guarda una tarea.
- `/queues`: Muestra el estado actual de todas las colas.
- `/dequeue/<priority>`: Elimina la tarea de la cola por FIFO.
- `/remove-task`: Elimina la tarea que se seleccione.

## IA utilizada:
- Modelo automatico Ml.

## Cómo correrlo
1. Instalar dependencias:
```bash
pip install -r requirements.txt
```
2.Ejecutar el modelo de entrenamiento si este no existe
python ml_model.py

3. Ejecutar el servidor:
```bash
python app.py

4.insertar tus tareas
