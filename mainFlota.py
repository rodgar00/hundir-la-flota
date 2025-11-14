def crear_tablero():
    tablero = []
    for i in range (10):
        tablero.append([])
        for j in range (10):
            tablero[i].append(" ")
    return tablero

def colocar_barcos(tablero, m, m2, m3, m4):
    print("Dime la posición a colocar entre paréntesis\n<< ")
    for barco in range(4):
        for acorazado in range(4):
            coords = (int(input("Introduce la primera")), int(input("Introduce la siguiente")))
            m[coords[0]][coords[1]] = "*"
            m2[coords[0]][coords[1]] = "*"
            m3[coords[0]][coords[1]] = "*"
            m4[coords[0]][coords[1]] = "*"
        return coords
    return tablero

def printMatriz(tablero):
    for fila in tablero:
        print(fila)

mi_tablero = crear_tablero()
mi_tablero_con_barcos = colocar_barcos(mi_tablero)

printMatriz(mi_tablero_con_barcos)