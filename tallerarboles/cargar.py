import pandas as pd

class Hospital:
    def __init__(self,nombre:str, nit:int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio

    def __str__(self):
        return f"Nombre: {self.nombre}, NIT:{self.nit}, Sede:{self.sede}, Municipio:{self.municipio}"

class Nodo:
    def __init__(self,hospital: Hospital):
        self.hospital = hospital
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, hospital):
        if self.raiz is None:
            self.raiz = Nodo(hospital)
        else:
            self._insertar(hospital, self.raiz)

    def _insertar(self, hospital, nodo):
        if hospital.nit < nodo.hospital.nit:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(hospital)
            else:
                self._insertar(hospital, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(hospital)
            else:
                self._insertar(hospital, nodo.derecha)

    def buscar(self, nit):
        return self._buscar(nit, self.raiz)

    def _buscar(self, nit, nodo):
        if nodo is None:
            return None
        if nit == nodo.hospital.nit:
            return nodo
        elif nit < nodo.hospital.nit:
            return self._buscar(nit, nodo.izquierda)
        else:
            return self._buscar(nit, nodo.derecha)
        
    def inorden(self):
        
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo.izquierda is not None:
            self._inorden(nodo.izquierda)
        print(nodo.hospital)
        if nodo.derecha is not None:
            self._inorden(nodo.derecha)

hospitales = pd.read_csv('/workspaces/estructura_datos/tallerarboles/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv')
hospitales.rename(columns={'Razón Social Organización': 'nombre2',
                           'Número NIT': 'nit',
                           'Nombre Sede': 'sede',
                           'Nombre Municipio': 'municipio'}, inplace=True)
hospitales['nit'] = hospitales['nit'].str.replace(',','')
hospitales['nit'] = hospitales['nit'].astype(int)

# Crear árbol e insertar hospitales
arbol = ArbolBinario()

for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['nombre2'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    arbol.insertar(hospital)

# Menú
while True:
    print("\n--- MENÚ ---")
    print("1. Buscar hospital por NIT")
    print("2. Recorrido en orden")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nit = int(input("Ingrese el NIT del hospital: "))
        nodo = arbol.buscar(nit)
        if nodo is not None:
            print("\nHospital encontrado:")
            print(nodo.hospital)
        else:
            print("\nNo se encontró un hospital con ese NIT.")
    
    elif opcion == "2":
        print("\n--- Recorrido en orden ---")
        arbol.inorden()  # Imprime todos los hospitales en orden
    
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida.")