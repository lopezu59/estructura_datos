import json

class Queue:
    def __init__(self) -> None:
        self.front = 0
        self.rear = 0
        self.items = {}

    def enqueue(self, task: str, priority: str):
        self.items[self.rear] = {
            "task": task,
            "priority": priority
        }
        self.rear += 1

    def dequeue(self, priority: str): 
        priority = priority.capitalize()
        for i in range(self.front, self.rear):
            if self.items[i]["priority"] == priority:
                item = self.items[i]
                new_items = {}
                new_rear = 0
                for j in range(self.front, self.rear):
                    if j == i:
                        continue
                    new_items[new_rear] = self.items[j]
                    new_rear += 1
                self.items = new_items
                self.front = 0
                self.rear = new_rear
                return item
        return None 

    def is_empty(self):
        return self.front == self.rear

    def to_list(self):
        return [self.items[i] for i in range(self.front, self.rear)]

    def remove(self, task_description: str) -> bool:
        new_items = {}
        new_rear = 0
        removed = False

        for i in range(self.front, self.rear):
            if self.items[i]["task"] == task_description and not removed:
                removed = True
                continue
            new_items[new_rear] = self.items[i]
            new_rear += 1

        self.items = new_items
        self.front = 0
        self.rear = new_rear
        return removed

task_queue = Queue()  #una sola cola

# Función para guardar las colas en archivo JSON
def save_queue():
    data = task_queue.to_list() 
    with open('queue.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Función para cargar las colas desde el archivo JSON
def load_queue():
    try:
        with open('queue.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                task = item.get('task')
                priority = item.get('priority')
                task_queue.enqueue(task, priority)
    except FileNotFoundError:
        pass  # Si el archivo no existe, simplemente no hacemos nada
