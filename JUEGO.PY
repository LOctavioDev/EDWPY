def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, simbolo):
    for fila in tablero:
        if all(s == simbolo for s in fila):
            return True
    for columna in range(3):
        if all(tablero[fila][columna] == simbolo for fila in range(3)):
            return True
    if all(tablero[i][i] == simbolo for i in range(3)) or all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def juego_tateti():
    tablero = inicializar_tablero()
    jugador = "X"
    jugadas = 0

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador}")
        fila = int(input("Ingresa la fila (0, 1, 2): "))
        columna = int(input("Ingresa la columna (0, 1, 2): "))

        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            jugadas += 1

            if jugadas >= 5 and verificar_ganador(tablero, jugador):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador} ha ganado!")
                break
            elif jugadas == 9:
                imprimir_tablero(tablero)
                print("¡Empate!")
                break

            jugador = "O" if jugador == "X" else "X"
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")

if __name__ == "__main__":
    juego_tateti()
