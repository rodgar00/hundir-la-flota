import socket

# ---- FUNCIONES DEL TABLERO ----
def crear_tablero():
    return [[" "]*10 for _ in range(10)]

def comprobarCoords(tablero, *coords):
    for (fila, columna) in coords:
        if fila < 0 or fila >= 10 or columna < 0 or columna >= 10:
            raise IndexError("Coordenadas fuera del tablero.")
    return True

def printMatriz(tablero):
    for fila in tablero:
        print(fila)

def colocar_barcos(tablero):
    print("Coloca tus barcos")
    colocado = False
    while not colocado:
        try:
            # LANCHA
            fila = int(input("Fila lancha: "))
            col = int(input("Columna lancha: "))
            comprobarCoords(tablero, (fila, col))
            tablero[fila][col] = "*"

            # CORBETA
            fila = int(input("Fila corbeta: "))
            col = int(input("Columna corbeta: "))
            comprobarCoords(tablero, (fila, col))
            tablero[fila][col] = "*"
            dir = int(input("Dirección (1 Arriba,2 Derecha,3 Abajo,4 Izquierda): "))
            if dir==1: f1,c1=fila-1,col
            elif dir==2: f1,c1=fila,col+1
            elif dir==3: f1,c1=fila+1,col
            else: f1,c1=fila,col-1
            comprobarCoords(tablero,(f1,c1))
            tablero[f1][c1]="*"

            # FRAGATA
            fila = int(input("Fila fragata: "))
            col = int(input("Col fragata: "))
            comprobarCoords(tablero,(fila,col))
            tablero[fila][col]="*"
            dir=int(input("Dirección: "))
            if dir==1:c1=(fila-1,col);c2=(fila-2,col)
            elif dir==2:c1=(fila,col+1);c2=(fila,col+2)
            elif dir==3:c1=(fila+1,col);c2=(fila+2,col)
            else:c1=(fila,col-1);c2=(fila,col-2)
            comprobarCoords(tablero,c1,c2)
            tablero[c1[0]][c1[1]]="*"
            tablero[c2[0]][c2[1]]="*"

            # ACORAZADO
            fila=int(input("Fila acorazado: "))
            col=int(input("Col acorazado: "))
            comprobarCoords(tablero,(fila,col))
            tablero[fila][col]="*"
            dir=int(input("Dirección: "))
            if dir==1:c1=(fila-1,col);c2=(fila-2,col);c3=(fila-3,col)
            elif dir==2:c1=(fila,col+1);c2=(fila,col+2);c3=(fila,col+3)
            elif dir==3:c1=(fila+1,col);c2=(fila+2,col);c3=(fila+3,col)
            else:c1=(fila,col-1);c2=(fila,col-2);c3=(fila,col-3)
            comprobarCoords(tablero,c1,c2,c3)
            tablero[c1[0]][c1[1]]="*";tablero[c2[0]][c2[1]]="*";tablero[c3[0]][c3[1]]="*"

            colocado=True
        except:
            print("Error, vuelve a intentarlo")
    return tablero

# ---- CLIENTE ----
cliente=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

tablero=colocar_barcos(crear_tablero())
print("Tu tablero:")
printMatriz(tablero)

# Enviar tablero
tablero_str="|".join(["".join(fila) for fila in tablero])
cliente.sendto(("TABLERO_J2|"+tablero_str).encode(),("127.0.0.1",5005))

# Esperar confirmación
while True:
    data,_=cliente.recvfrom(1024)
    msg=data.decode()
    if "OK TABLERO" in msg:
        print(msg)
        break

print("Tablero confirmado por el servidor. Comienza la partida.")

# Bucle de juego
while True:
    coords=input("Dispara (fila,col): ")
    if "," not in coords:
        print("Error: formato fila,columna")
        continue
    cliente.sendto(("J2|"+coords).encode(),("127.0.0.1",5005))
    data,_=cliente.recvfrom(1024)
    msg=data.decode()
    print("Servidor:",msg)
    if "GANADOR" in msg:
        print("¡Fin de la partida!")
        break
