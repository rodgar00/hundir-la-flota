def crear_tablero():
    tablero = []
    for i in range (10):
        tablero.append([])
        for j in range (10):
            tablero[i].append(0)
    return tablero

def colocar_barcos(tablero):
    return tablero

def printMatriz(tablero):
    for fila in tablero:
        print(fila)

mi_tablero = crear_tablero()
mi_tablero_con_barcos = colocar_barcos(mi_tablero)

printMatriz(mi_tablero_con_barcos)