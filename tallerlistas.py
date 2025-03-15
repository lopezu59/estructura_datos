class Animal:
    def __init__(self, nombre: str, edad: int, tipo_animal: str):
        self.nombre = nombre
        self.edad = edad
        self.tipo_animal = tipo_animal

#Los getters nos permiten leer valores de un atributo
    def get_nombre(self):
        return self.nombre 
    
    def get_edad(self):
        return self.edad
    
    def get_tipo_animal(self):
        return self.tipo_animal
    
#Los setters nos permiten modificar valores de un atributo
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_tipo_animal(self, tipo_animal):
        self.tipo_animal = tipo_animal
 
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo de Animal: {self.tipo_animal}"

class Node:
    def __init__(self, data: Animal) -> None:
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def agregar_animales(self) -> None:
        for _ in range(2):
            nombre = input("Ingrese el nombre del animal: ")
            edad = int(input("Ingrese la edad del animal: "))
            tipo_animal = input("Ingrese el tipo de animal: ")
            
            animal = Animal(nombre, edad, tipo_animal)
            
            if self.existe_animal(animal):
                print("El animal ya está en la lista y no puede ser añadido nuevamente.")
                continue
            
            self.agregar_animal(animal)
            print("Animal agregado correctamente.")
    
    def agregar_animal(self, animal: Animal) -> None:
        nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = nodo
    
    def existe_animal(self, animal: Animal) -> bool:
        actual = self.cabeza
        while actual:
            if actual.data.get_nombre() == animal.get_nombre() and actual.data.get_tipo_animal() == animal.get_tipo_animal():
                return True
            actual = actual.next
        return False
    
    def mostrar_animales_iterativo(self) -> None:
        actual = self.cabeza
        while actual:
            print(actual.data)
            actual = actual.next
    
    def mostrar_animales_recursivo(self, nodo=None) -> None:
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return  # Caso base: si la lista está vacía o se llega al final
        print(nodo.data)
        self.mostrar_animales_recursivo(nodo.next)

lista_animales = ListaEnlazada()
lista_animales.agregar_animales()

print("\nAnimales registrados (Iterativo):")
lista_animales.mostrar_animales_iterativo()

print("\nAnimales registrados (Recursivo):")
lista_animales.mostrar_animales_recursivo()


#ejercicio 2
