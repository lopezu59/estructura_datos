from typing import Optional

class Node:
    def __init__(self, numero:int) -> None:
        self.dato = numero
        self.next: Optional["Node"] = None

class ListaEnlazada:
    def __init__(self)->None:
        self.cabeza: Optional["Node"] = None
        
    def agregar_nodo(self, numero:int)->None:
        nodo: Node = Node(numero)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            self.cabeza = nodo
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next  
            nodo_actual.next = nodo
            print(ListaEnlazada(5))
            
lista = ListaEnlazada()
# print(lista.agregar_nodo(5))
# print(lista.agregar_nodo(10))
# print(lista.agregar_nodo(15))
# print(lista.agregar_nodo(25))            

    # def es_vacio(self):
    #     return self.cabeza is None
    

                
    # def eliminar(self,dato):
    #     nodo_actual = self.cabeza
    #     if nodo_actual.data == dato:
    #         self.cabeza = nodo_actual.next
    #         return
    #     while nodo_actual.next is not None:
    #         if nodo_actual.next.data == dato:
    #             nodo_actual.next = nodo_actual.next.next
    #             return
    #         nodo_actual = nodo_actual.next
            
    # def imprimir(self):
    #     nodo_actual = self.cabeza
    #     while nodo_actual is not None:
    #         print(nodo_actual.data)
    #         nodo_actual = nodo_actual.next

