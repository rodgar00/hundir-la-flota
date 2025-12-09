import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5005))

print("Servidor esperando tableros...")

tablero_j1 = None
tablero_j2 = None
turno = "J1"

partida_activa = True

def parse_tablero(texto):
    filas = texto.split("|")
    matriz = []
    for f in filas:
        matriz.append(list(f))
    return matriz

def disparo(matriz, f, c):
    if matriz[f][c] == "*":
        matriz[f][c] = "X"
        return "tocado"
    else:
        return "agua"

def quedan_barcos(tablero):
    for fila in tablero:
        if "*" in fila:
            return True
    return False

while partida_activa:
    datos, addr = server.recvfrom(10000)
    mensaje = datos.decode()

    if mensaje.startswith("TABLERO_J1|"):
        tablero_j1 = parse_tablero(mensaje.split("|", 1)[1])
        server.sendto(b"OK TABLERO_J1", addr)
        print("Tablero J1 recibido")
        continue

    if mensaje.startswith("TABLERO_J2|"):
        tablero_j2 = parse_tablero(mensaje.split("|", 1)[1])
        server.sendto(b"OK TABLERO_J2", addr)
        print("Tablero J2 recibido")
        continue

    if tablero_j1 is None or tablero_j2 is None:
        server.sendto(b"Aun no estan los dos tableros", addr)
        continue

    try:
        jugador, coords = mensaje.split("|")
        f_str, c_str = coords.split(",")
        f, c = int(f_str), int(c_str)
    except:
        server.sendto(b"Error: coordenadas invalidas, usa fila,columna", addr)
        continue

    if jugador != turno:
        server.sendto(b"No es tu turno", addr)
        continue

    if jugador == "J1":
        resultado = disparo(tablero_j2, f, c)
        if not quedan_barcos(tablero_j2):
            server.sendto(b"GANADOR: J1", addr)
            partida_activa = False
            continue
        turno = "J2"
    else:
        resultado = disparo(tablero_j1, f, c)
        if not quedan_barcos(tablero_j1):
            server.sendto(b"GANADOR: J2", addr)
            print("J2 ha ganado")
            partida_activa = False
            continue
        turno = "J1"

    server.sendto(f"Resultado: {resultado} | Turno: {turno}".encode(), addr)
