from flask import Flask, request, jsonify, render_template
from task_classifier import classify_task
from queues import task_queue, save_queue, load_queue

app = Flask(__name__)

# Cargar tareas al iniciar
load_queue()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task', '').strip()
    if not task:
        return jsonify({'error': 'No task provided'}), 400

    priority = classify_task(task)
    task_queue.enqueue(task, priority)
    save_queue()

    return jsonify({
        'message': 'Task added successfully',
        'task': task,
        'classified_as': priority
    })

@app.route('/queues', methods=['GET'])
def get_queues():
    # Clasificar tareas por prioridad para enviarlas al frontend
    organized = {'Alta': [], 'Media': [], 'Baja': []}
    for item in task_queue.to_list():
        organized[item['priority']].append(item['task'])
    return jsonify(organized)

@app.route('/dequeue/<priority>', methods=['POST'])
def dequeue_task(priority):
    removed = task_queue.dequeue(priority.capitalize())
    if removed:
        save_queue()
        return jsonify({'message': 'Tarea eliminada correctamente', 'task': removed['task']})
    else:
        return jsonify({'error': 'No hay tareas en esa cola'}), 404


@app.route('/remove-task', methods=['POST'])
def remove_task():
    data = request.get_json()
    priority = data.get('priority', '').capitalize()
    task_desc = data.get('task', '')

    if not task_desc or not priority:
        return jsonify({'error': 'Missing task or priority'}), 400

    removed = task_queue.remove(task_desc)
    if removed:
        save_queue()
        return jsonify({'message': 'Task removed successfully', 'task': task_desc})
    else:
        return jsonify({'error': 'Task not found in queue'}), 404

if __name__ == '__main__':
    app.run(debug=True)
