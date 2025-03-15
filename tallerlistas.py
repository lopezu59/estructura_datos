class Animal:
    def __init__(self, nombre: str, edad: int, tipo_animal: str):
        self._nombre = None # Se inicializan los atributos en None para forzar el uso de los setters
        self._edad = None
        self._tipo_animal = None

        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_tipo_animal(tipo_animal)

#Los getters nos permiten leer valores de un atributo
    def get_nombre(self):
        return self._nombre 
    
    def get_edad(self):
        return self._edad
    
    def get_tipo_animal(self):
        return self._tipo_animal
    
#Los setters nos permiten modificar valores de un atributo o como en este caso validar que un valor sea correcto
    def set_nombre(self, nombre):
      if isinstance (nombre, str) and nombre.strip(): #los isintance nos permite validar si el valor es del tipo que queremos y los strip nos permite validar si el valor no es vacio
          self._nombre = nombre
      else:
        print("El nombre no es válido")

    def set_edad(self, edad):
        if isinstance (edad, int) and edad > 0:
            self._edad = edad
        else:
            print("La edad no es válida") 

    def set_tipo_animal(self, tipo_animal):
        if isinstance (tipo_animal, str) and tipo_animal.strip():
            self._tipo_animal = tipo_animal
        else:
            print("El tipo de animal no es válido")
 
    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Tipo de Animal: {self._tipo_animal}"

class Node:
    def __init__(self, data: Animal) -> None:
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def agregar_animal(self):
     while True:   
        nombre = input("Ingrese el nombre del animal: ")
        edad_input = int(input("Ingrese la edad del animal: "))
        tipo_animal = input("Ingrese el tipo de animal: ")
        
        if edad_input == 0 or edad_input < -1:
            print("Error: La edad debe ser un número entero positivo.")
            continue
        
        edad = int(edad_input)
        animal = Animal(nombre, edad, tipo_animal)

        if animal.get_nombre() is None or animal.get_edad() is None or animal.get_tipo_animal() is None:
                print("Error: No se pudo agregar el animal debido a datos inválidos.")
                continue 

        if self.existe_animal(animal):
            print("El animal ya está en la lista y no puede ser añadido nuevamente.")
            return
        
        nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = nodo
        print("Animal agregado correctamente.")
        break
    
    def existe_animal(self, animal: Animal) -> bool:
        actual = self.cabeza
        while actual:
            if actual.data.get_nombre() == animal.get_nombre() or actual.data.get_tipo_animal() == animal.get_tipo_animal():
                return True
            actual = actual.next
        return False
    
    #No almacena los datos previos en pila de ejecución, solo se almacena el nodo actual
    def mostrar_animales_iterativo(self) -> None:
        actual = self.cabeza
        while actual:
            print(actual.data)
            actual = actual.next


     #Se almacena en pila de ejecución la llamada a la función con el nodo actual
    def mostrar_animales_recursivo(self, nodo=None) -> None: 
        if nodo is None: 
            nodo = self.cabeza
        if nodo is None:
            return  
        print(nodo.data)
        if nodo.next is not None:  
            self.mostrar_animales_recursivo(nodo.next) 

lista_animales = ListaEnlazada()

while True:
    opcion = input("¿Desea agregar un animal? (s/n): ")
    if opcion.lower() != 's':
        break
    lista_animales.agregar_animal()

print("\nAnimales registrados (Iterativo):")
lista_animales.mostrar_animales_iterativo()

print("\nAnimales registrados (Recursivo):")
lista_animales.mostrar_animales_recursivo()


#ejercicio 2
