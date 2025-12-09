import socket

# ---- FUNCIONES DEL TABLERO ----
def crear_tablero():
    return [[" "]*10 for _ in range(10)]

def comprobarCoords(tablero, *coords):
    for (fila, columna) in coords:
        if fila < 0 or fila >= 10 or columna < 0 or columna >= 10:
            raise IndexError("Coordenadas fuera del tablero.")
    return True

def printMatrizConCoords(tablero):
    print("   " + " ".join(str(i) for i in range(10)))  # columnas
    for i, fila in enumerate(tablero):
        print(f"{i}  " + " ".join(fila))

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
            direccion = int(input("Dirección (1 Arriba,2 Derecha,3 Abajo,4 Izquierda): "))
            if direccion==1: f1,c1=fila-1,col
            elif direccion==2: f1,c1=fila,col+1
            elif direccion==3: f1,c1=fila+1,col
            else: f1,c1=fila,col-1
            comprobarCoords(tablero,(f1,c1))
            tablero[f1][c1]="*"

            # FRAGATA
            fila = int(input("Fila fragata: "))
            col = int(input("Columna fragata: "))
            comprobarCoords(tablero,(fila,col))
            tablero[fila][col]="*"
            direccion=int(input("Dirección: "))
            if direccion==1:c1=(fila-1,col);c2=(fila-2,col)
            elif direccion==2:c1=(fila,col+1);c2=(fila,col+2)
            elif direccion==3:c1=(fila+1,col);c2=(fila+2,col)
            else:c1=(fila,col-1);c2=(fila,col-2)
            comprobarCoords(tablero,c1,c2)
            tablero[c1[0]][c1[1]]="*"
            tablero[c2[0]][c2[1]]="*"

            # ACORAZADO
            fila=int(input("Fila acorazado: "))
            col=int(input("Columna acorazado: "))
            comprobarCoords(tablero,(fila,col))
            tablero[fila][col]="*"
            direccion=int(input("Direccion: "))
            if direccion==1:c1=(fila-1,col);c2=(fila-2,col);c3=(fila-3,col)
            elif direccion==2:c1=(fila,col+1);c2=(fila,col+2);c3=(fila,col+3)
            elif direccion==3:c1=(fila+1,col);c2=(fila+2,col);c3=(fila+3,col)
            else:c1=(fila,col-1);c2=(fila,col-2);c3=(fila,col-3)
            comprobarCoords(tablero,c1,c2,c3)
            tablero[c1[0]][c1[1]]="*";tablero[c2[0]][c2[1]]="*";tablero[c3[0]][c3[1]]="*"

            colocado=True
        except:
            print("Error, vuelve a intentarlo")
    return tablero

def actualizar_tablero_rival(tablero_rival, fila, col, resultado):
    if resultado == "tocado":
        tablero_rival[fila][col] = "X"
    elif resultado == "agua":
        tablero_rival[fila][col] = "O"

# ---- CLIENTE ----
cliente=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

tablero=colocar_barcos(crear_tablero())
print("Tu tablero:")
printMatrizConCoords(tablero)

tablero_rival=crear_tablero()

# Enviar tablero
tablero_str="|".join(["".join(fila) for fila in tablero])
cliente.sendto(("TABLERO_J1|"+tablero_str).encode(),("127.0.0.1",5005))

# Esperar confirmación
while True:
    data,_=cliente.recvfrom(1024)
    mensaje=data.decode()
    if "OK TABLERO" in mensaje:
        print(mensaje)
        break

print("Tablero confirmado por el servidor. Comienza la partida.")

# Bucle de juego
while True:
    coords=input("Dispara (fila,col): ")
    if "," not in coords:
        print("Error: formato fila,columna")
        continue
    try:
        f,c=map(int,coords.split(","))
    except:
        print("Error: coordenadas inválidas")
        continue

    cliente.sendto(("J1|"+coords).encode(),("127.0.0.1",5005))
    data,_=cliente.recvfrom(1024)
    mensaje=data.decode()
    print("Servidor:",mensaje)

    if "Resultado: " in mensaje:
        res=mensaje.split("Resultado: ")[1].split(" |")[0]
        actualizar_tablero_rival(tablero_rival,f,c,res)
        print("Tablero rival actualizado:")
        printMatrizConCoords(tablero_rival)

    if "GANADOR" in mensaje:
        print("¡Fin de la partida!")
        break
