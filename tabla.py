class Tablahash_tabla:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [] 
        self.contador = 0

    def agregar(self, key: str, value: str):
        if self.contador < self.tamaño:
            hash_clave = hash(key)
            self.tabla.append((key, value, hash_clave)) 
            print(f"\n Contacto agregado:")
            print(f"Nombre  : {key}")
            print(f"Teléfono: {value}")
            print(f"Hash    : {hash_clave}")
            print(f"Índice  : {self.contador}")
            self.contador += 1
        else:
            print("\n No hay espacio en la tabla para más contactos.")

def mostrar(self):
    print("\n Directorio Telefónico:")
    if not self.tabla:
        print("No hay contactos guardados.")
        return

    for i in range(len(self.tabla)):
        clave, value, hash_clave = self.tabla[i]
        print(f"Índice {i} | Hash: {hash_clave} → {clave}: {value}")

def buscar(self, clave: str):
    for i in range(len(self.tabla)):
        nombre, value, hash_clave = self.tabla[i]
        if nombre == clave:
            print("\n Contacto encontrado:")
            print(f"Nombre  : {nombre}")
            print(f"Teléfono: {value}")
            print(f"Hash    : {hash_clave}")
            print(f"Índice  : {i}")
            return
    print("\nContacto no encontrado.")

def eliminar(self, key: str):
    for i in range(len(self.tabla)):
        nombre, _, _ = self.tabla[i]
        if nombre == key:
            del self.tabla[i]
            self.contador -= 1
            print(f"\nContacto '{key}' eliminado.")
            return
    print("\nContacto no encontrado.")


def listar(self):
     if not self.tabla:
        print("\nNo hay contactos guardados.")
        return

     print("\nLista de contactos:")
     for key, value, _ in self.tabla:
            print(f"{key}: {value}")

tabla = Tablahash_tabla()
while True:
    opcion = input("\nSeleccione una opción digite ejemplo 1: 1.agregar, 2.buscar, 3.eliminar, 4.listar, 5.salir: ")
    if opcion == '5':
        break
    elif opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        tabla.agregar(nombre, telefono)
    elif opcion == '2':
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        tabla.buscar(nombre_buscar)
    elif opcion == '3':
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        tabla.eliminar(nombre_eliminar)
    elif opcion == '4':
        tabla.listar()
    else:
        print("Opción no válida.")
