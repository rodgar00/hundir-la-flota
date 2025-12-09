# Hundir la Flota - Python (Sockets)

Juego clásico de **Hundir la Flota** implementado en Python para **2 jugadores** usando **sockets**.  

Cada jugador coloca sus barcos en un tablero de 10x10 y dispara por turnos a las coordenadas del rival hasta hundir todos sus barcos.


## Cómo ejecutar

1. Ejecuta primero el servidor:
python server.py
Ejecuta cada cliente en una terminal separada:

Cada jugador coloca sus barcos siguiendo las instrucciones. Los barcos son:

Lancha (1 casilla)

Corbeta (2 casillas)

Fragata (3 casillas)

Acorazado (4 casillas)

Los tableros se muestran con coordenadas 0-9. El tablero del rival solo muestra X (tocado) y O (agua).

Luego los jugadores disparan por turnos usando coordenadas: fila,columna.

El juego termina cuando un jugador hunde todos los barcos del rival. El servidor anuncia el ganador.

Características
Sockets para comunicación entre servidor y clientes.

Colocación de barcos manual por cada jugador.

Tablero propio y tablero rival.

Indicador de resultados: tocado, agua y hundido.

Flujo de juego con turnos controlados y detección de ganador.

Manejo básico de errores de entrada y coordenadas fuera del tablero.

Ejemplo de tablero
   0 1 2 3 4 5 6 7 8 9
0  *       *          
1        *            
2                    
3  *                  
4                    
5                    
6                    
7                    
8                    
9                    
* → Barco propio
X → Tocado en tablero rival
O → Agua/fallo en tablero rival
