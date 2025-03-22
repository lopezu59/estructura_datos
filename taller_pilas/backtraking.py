# 0 = libre
# 1 = muro
# 3 = ruta
# 4 = ruta obsoleta

tablero = [
    [1, 0, 1, 1, 2],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def mostrar(tablero:int):
    for fila in tablero:
        for celda in fila:
            if celda == 3:
                print("X", end=" ")
            elif celda == 4:
                print(".", end=" ")  # Ruta descartada
            elif celda == 1:
                print("#", end=" ")  # Muro
            elif celda == 2:
                print("E", end=" ")  # Salida
            else:
                print("0", end=" ")  # Camino libre
        print()
    print()  # Espacio entre impresiones

def valido(i, j):
    return 0 <= i < len(tablero) and 0 <= j < len(tablero[0])  # Verifica límites

def buscar_con_pila(tablero, start_i, start_j):
    stack = [(start_i, start_j)]  # Pila con la posición inicial

    # Direcciones de movimiento: (fila, columna)
    movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Arriba, Izquierda, Abajo, Derecha

    while stack:
        i, j = stack.pop()  # Extraemos la última posición

        if not valido(i, j) or tablero[i][j] in (1, 3, 4):  
            continue  # Si es un muro o ya fue visitado, saltamos

        if tablero[i][j] == 2:  # Si encontramos la salida
            print("¡Encontró la salida!")
            mostrar(tablero)
            return True

        tablero[i][j] = 3  # Marcar como parte de la ruta

        # Agregar las posibles direcciones a la pila
        for di, dj in movimientos:
            stack.append((i + di, j + dj))

    # Si terminamos el ciclo sin encontrar la salida, marcamos rutas sin salida
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 3:
                tablero[i][j] = 4  # Marcar caminos sin salida

    print("No se encontró la salida.")
    return False

# Ejecutamos la búsqueda con pila desde la posición inicial (4,0)
buscar_con_pila(tablero, 4, 0)
mostrar(tablero)