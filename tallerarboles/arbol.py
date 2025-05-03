# Clase Nodo
class Nodo:
    def __init__(self, valor:int):
        self.valor = valor
        self.izq = None
        self.der = None

# Clase Árbol Binario de Búsqueda
class ArbolBinario:
    def __init__(self)->None:
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.der, valor)

    def mostrar_preorden_estructurado(self, nodo, prefijo="", es_ultimo=True):
        if nodo is not None:
            conector = "└── " if es_ultimo else "├── "
            print(prefijo + conector + str(nodo.valor))
            nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
            hijos = [nodo.izq, nodo.der]
            hijos_presentes = [h for h in hijos if h is not None]
            for i, hijo in enumerate(hijos_presentes):
                es_ultimo_hijo = (i == len(hijos_presentes) - 1)
                self.mostrar_preorden_estructurado(hijo, nuevo_prefijo, es_ultimo_hijo)

    def buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(nodo.izq, valor)
        else:
            return self.buscar(nodo.der, valor)


valores = [20, 10, 30, 5, 15, 25, 35]
arbol = ArbolBinario()
for v in valores:
    arbol.insertar(v)

print("Árbol en preorden:")
arbol.mostrar_preorden_estructurado(arbol.raiz)

while True:
    print("\n\n--- MENÚ ---")
    print("1. Buscar valor en el árbol")
    print("2. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        entrada = input("Ingrese el valor a buscar: ")
        try:
            valor = int(entrada)
            encontrado = arbol.buscar(arbol.raiz, valor)
            if encontrado:
                print(f"El valor {valor} está en el árbol.")
            else:
                print(f"El valor {valor} NO está en el árbol.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == "2":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")