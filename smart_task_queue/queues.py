import json

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def to_list(self):
        return list(self.items)

    def remove(self, item):
        try:
            self.items.remove(item)
            return True
        except ValueError:
            return False


# Diccionario de colas por prioridad (debe estar antes de cargar o guardar)
task_queues = {
    'Alta': Queue(),
    'Media': Queue(),
    'Baja': Queue()
}

# Función para guardar las colas en archivo JSON
def save_all_queues():
    data = {prio: queue.to_list() for prio, queue in task_queues.items()}
    with open('queues.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Función para cargar las colas desde el archivo JSON
def load_all_queues():
    try:
        with open('queues.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for prio, tasks in data.items():
                task_queues[prio].items = tasks
    except FileNotFoundError:
        # Si el archivo no existe, iniciar con colas vacías
        pass

# Cargar las colas al iniciar la app
load_all_queues()
