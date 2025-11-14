def crear_tablero():
    tablero = []
    for i in range(10):
        tablero.append([])
        for j in range(10):
            tablero[i].append(" ")
    return tablero


def comprobarCoords(tablero, *coords):
    for (fila, columna) in coords:
        if fila < 0 or fila >= 10 or columna < 0 or columna >= 10:
            raise IndexError("Coordenadas fuera del tablero.")
    return True


def printMatriz(tablero):
    for fila in tablero:
        print(fila)


def colocar_barcos(tablero):
    print("Dime la posición a colocar (fila y columna)")
    colocado = False

    while not colocado:
        try:
            # LANCHA
            fila = int(input("Introduce la fila de tu lancha (0-9): "))
            columna = int(input("Introduce la columna de tu lancha (0-9): "))
            comprobarCoords(tablero, (fila, columna))
            tablero[fila][columna] = "*"

            # CORBETA
            fila = int(input("Introduce la fila de tu corbeta (0-9): "))
            columna = int(input("Introduce la columna de tu corbeta (0-9): "))
            comprobarCoords(tablero, (fila, columna))
            tablero[fila][columna] = "*"

            direccion = int(input("¿En qué dirección? \n1. Arriba\n2. Derecha\n3. Abajo\n4. Izquierda\n>> "))

            if direccion == 1:   # arriba
                coordsFinal1 = (fila - 1, columna)
            elif direccion == 2:  # derecha
                coordsFinal1 = (fila, columna + 1)
            elif direccion == 3:  # abajo
                coordsFinal1 = (fila + 1, columna)
            elif direccion == 4:  # izquierda
                coordsFinal1 = (fila, columna - 1)
            else:
                raise ValueError("Dirección inválida")

            comprobarCoords(tablero, coordsFinal1)
            tablero[coordsFinal1[0]][coordsFinal1[1]] = "*"

            # FRAGATA
            fila = int(input("Introduce la fila de tu fragata (0-9): "))
            columna = int(input("Introduce la columna de tu fragata (0-9): "))
            comprobarCoords(tablero, (fila, columna))
            tablero[fila][columna] = "*"

            direccion = int(input("¿En qué dirección? \n1. Arriba\n2. Derecha\n3. Abajo\n4. Izquierda\n>> "))

            if direccion == 1:
                coordsFinal1 = (fila - 1, columna)
                coordsFinal2 = (fila - 2, columna)
            elif direccion == 2:
                coordsFinal1 = (fila, columna + 1)
                coordsFinal2 = (fila, columna + 2)
            elif direccion == 3:
                coordsFinal1 = (fila + 1, columna)
                coordsFinal2 = (fila + 2, columna)
            elif direccion == 4:
                coordsFinal1 = (fila, columna - 1)
                coordsFinal2 = (fila, columna - 2)
            else:
                raise ValueError("Dirección inválida")

            comprobarCoords(tablero, coordsFinal1, coordsFinal2)
            tablero[coordsFinal1[0]][coordsFinal1[1]] = "*"
            tablero[coordsFinal2[0]][coordsFinal2[1]] = "*"

            # ACORAZADO
            fila = int(input("Introduce la fila de tu acorazado (0-9): "))
            columna = int(input("Introduce la columna de tu acorazado (0-9): "))
            comprobarCoords(tablero, (fila, columna))
            tablero[fila][columna] = "*"

            direccion = int(input("¿En qué dirección? \n1. Arriba\n2. Derecha\n3. Abajo\n4. Izquierda\n>> "))

            if direccion == 1:
                coordsFinal1 = (fila - 1, columna)
                coordsFinal2 = (fila - 2, columna)
                coordsFinal3 = (fila - 3, columna)
            elif direccion == 2:
                coordsFinal1 = (fila, columna + 1)
                coordsFinal2 = (fila, columna + 2)
                coordsFinal3 = (fila, columna + 3)
            elif direccion == 3:
                coordsFinal1 = (fila + 1, columna)
                coordsFinal2 = (fila + 2, columna)
                coordsFinal3 = (fila + 3, columna)
            elif direccion == 4:
                coordsFinal1 = (fila, columna - 1)
                coordsFinal2 = (fila, columna - 2)
                coordsFinal3 = (fila, columna - 3)
            else:
                raise ValueError("Dirección inválida")

            comprobarCoords(tablero, coordsFinal1, coordsFinal2, coordsFinal3)

            tablero[coordsFinal1[0]][coordsFinal1[1]] = "*"
            tablero[coordsFinal2[0]][coordsFinal2[1]] = "*"
            tablero[coordsFinal3[0]][coordsFinal3[1]] = "*"

            colocado = True

        except (ValueError, IndexError):
            print("Error: Entrada no válida. Inténtalo de nuevo.\n")

    return tablero


mi_tablero = crear_tablero()
mi_tablero_con_barcos = colocar_barcos(mi_tablero)
printMatriz(mi_tablero_con_barcos)
