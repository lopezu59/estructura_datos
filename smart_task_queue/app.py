from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify
from task_classifier import classify_task
from queues import task_queues
from queues import load_all_queues, save_all_queues

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task', '')
    if not task:
        return jsonify({'error': 'No task provided'}), 400

    priority = classify_task(task)
    task_queues[priority].enqueue(task)

    save_all_queues()  # Guardar cada vez que agregas tarea

    return jsonify({
        'message': 'Task added successfully',
        'task': task,
        'classified_as': priority
    })

@app.route('/queues', methods=['GET'])
def get_queues():
    return jsonify({
        'Alta': task_queues['Alta'].to_list(),
        'Media': task_queues['Media'].to_list(),
        'Baja': task_queues['Baja'].to_list()
    })

@app.route('/dequeue/<priority>', methods=['POST'])
def dequeue_task(priority):
    priority = priority.capitalize()
    if priority not in task_queues:
        return jsonify({'error': 'Invalid priority level'}), 400

    task = task_queues[priority].dequeue()
    if task is None:
        return jsonify({'message': f'No tasks in {priority} queue'}), 200

    save_all_queues()  # Guardar al eliminar la primera tarea de la cola

    return jsonify({'message': f'Task removed from {priority} queue', 'task': task})

@app.route('/remove-task', methods=['POST'])
def remove_task():
    data = request.get_json()
    priority = data.get('priority', '').capitalize()
    task_desc = data.get('task', '')

    if priority not in task_queues:
        return jsonify({'error': 'Invalid priority level'}), 400
    if not task_desc:
        return jsonify({'error': 'No task description provided'}), 400

    removed = task_queues[priority].remove(task_desc)
    if removed:
        save_all_queues()  # Guardar cambios
        return jsonify({'message': 'Task removed successfully', 'task': task_desc})
    else:
        return jsonify({'error': 'Task not found in queue'}), 404

if __name__ == '__main__':
    app.run(debug=True)