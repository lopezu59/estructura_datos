import json

class Node:
    def __init__(self, task:str, priority:str):
        self.task = task
        self.priority = priority
        self.next = None

class Queue:
    def __init__(self)->None:
        self.front = None  # Apuntador al frente de la cola
        self.rear = None   # Apuntador al final de la cola

    def is_empty(self)->bool:
        return self.front is None

    def enqueue(self, task, priority):
        new_node = Node(task, priority)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self, priority:str):
        if self.is_empty():
            return None

        current = self.front
        previous = None

        while current:
            if current.priority == priority:
                if previous is None:
                    # El nodo a eliminar es el primero
                    self.front = current.next
                else:
                    previous.next = current.next

                if current == self.rear:
                    self.rear = previous

                return {"task": current.task, "priority": current.priority}

            previous = current
            current = current.next

        return None

    def to_list(self)->list:
       # Convierte la cola a una lista de diccionarios.
        result = []
        current = self.front
        while current:
            result.append({"task": current.task, "priority": current.priority})
            current = current.next
        return result

    def remove(self, task_description:str):
        if self.is_empty():
            return False

        current = self.front
        previous = None

        while current:
            if current.task == task_description:
                if previous is None:
                    self.front = current.next
                else:
                    previous.next = current.next

                if current == self.rear:
                    self.rear = previous

                return True

            previous = current
            current = current.next

        return False

task_queue = Queue()  #una sola cola

# Función para guardar las cola en archivo JSON
def save_queue():
    data = []
    current = task_queue.front
    while current:
        data.append({
            'task': current.task,
            'priority': current.priority
        })
        current = current.next
    with open('queue.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Función para cargar las colas desde el archivo JSON
def load_queue():
    try:
        with open('queue.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                task_queue.enqueue(item['task'], item['priority'])
    except FileNotFoundError:
        pass # Si el archivo no existe, simplemente no hacemos nada
