class Nodo:
    def __init__(self, valor:int, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

class ArbolBinario:
    def __init__(self, raiz=None)->None:
        self.raiz = raiz

    def insertar(self, valor)->None:
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo)->None:
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def buscar(self, valor)->bool:
        if self.raiz is None:
            return False
        else:
            return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo)->bool:
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor and nodo.izq is not None:
            return self._buscar(valor, nodo.izq)
        elif valor > nodo.valor and nodo.der is not None:
            return self._buscar(valor, nodo.der)
        return False
    
    def preorden(self)->None:
        if self.raiz is not None:
            self._preorden(self.raiz)

    def _preorden(self, nodo)->None:
        print(nodo.valor)
        if nodo.izq is not None:
            self._preorden(nodo.izq)
        if nodo.der is not None:
            self._preorden(nodo.der)

valores = [20, 10, 30, 5, 15, 25, 35]
arbol = ArbolBinario()
for v in valores:
    arbol.insertar(v)

# Menú interactivo
while True:
    print("\n--- MENÚ ---")
    print("1. Ver números")
    print("2. Buscar un número")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("Números en el árbol (preorden):")
        arbol.preorden()
    elif opcion == "2":
        try:
            num = int(input("Número a buscar: "))
            if arbol.buscar(num):
                print(f"El número {num} SÍ está en el árbol.")
            else:
                print(f"El número {num} NO está en el árbol.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
