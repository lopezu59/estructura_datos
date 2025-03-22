def push(pila, tope, max):
    if tope >= max:
        print("Pila llena, no se puede insertar más elementos")
    else:
        dato = int(input("Ingrese un número a apilar: "))
        pila[tope] = dato
        tope += 1
    return tope

def pop(pila, tope):
    if isEmpty(tope):
        print("Pila vacía, no hay elementos para eliminar")
    else:
        tope -= 1
        print("Elemento eliminado:", pila[tope])
    return tope

def peek(pila, tope):
    if isEmpty(tope):
        print("La pila está vacía, no hay elementos en la cima")
    else:
        print("El elemento en la cima es:", pila[tope - 1])

def isEmpty(tope):
    return tope == 0

def mostrarPila(pila, tope):
    if isEmpty(tope):
        print("La pila está vacía, no hay elementos para mostrar")
    else:
        print("Elementos en la pila:")
        for i in range(tope - 1, -1, -1):
            print(f"Posición {i + 1}: {pila[i]}")

def main():
    max = 5
    tope = 0  # En Python, los índices de listas comienzan en 0
    pila = [None] * max  # Se inicializa la pila con valores vacíos
    
    while True:
        print("\n----- MENÚ PILA -----")
        print("1. Insertar (push)")
        print("2. Eliminar (pop)")
        print("3. Ver tope (peek)")
        print("4. Ver si está vacía (isEmpty)")
        print("5. Mostrar todos los elementos")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            tope = push(pila, tope, max)
        elif opcion == 2:
            tope = pop(pila, tope)
        elif opcion == 3:
            peek(pila, tope)
        elif opcion == 4:
            if isEmpty(tope):
                print("La pila está vacía")
            else:
                print("La pila tiene elementos")
        elif opcion == 5:
            mostrarPila(pila, tope)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

main()
