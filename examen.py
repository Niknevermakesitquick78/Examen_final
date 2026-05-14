import random

class TresEnRaya:
    def __init__(self, nacho, esqueleto):
        self.nacho = nacho
        self.esqueleto = esqueleto

        self.tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        if random.randint(1, 2) == 1:
            self.jugador_actual = nacho
            self.simbolo_actual = "X"
        else:
            self.jugador_actual = esqueleto
            self.simbolo_actual = "O"

        self.juego_activo = True

    def mostrar_tablero(self, con_numeros=True):
        numero = 1

        for fila in range(3):
            linea = ""

            for columna in range(3):
                valor = self.tablero[fila][columna]

                if valor == " " and con_numeros:
                    linea += str(numero)
                else:
                    linea += valor

                if columna < 2:
                    linea += " | "

                numero += 1

            print(linea)

            if fila < 2:
                print("---------")

    def colocar_ficha(self, posicion):
        if posicion < 1 or posicion > 9:
            print("Esa posicion no existe en el ring.")
            return False

        fila = (posicion - 1) // 3
        columna = (posicion - 1) % 3

        if self.tablero[fila][columna] != " ":
            print("Esa posicion ya tiene poder luchador.")
            return False

        self.tablero[fila][columna] = self.simbolo_actual
        return True

    def verificar_ganador(self):
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != " ":
                return fila[0]

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != " ":
                return self.tablero[0][columna]

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != " ":
            return self.tablero[0][0]

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != " ":
            return self.tablero[0][2]

        return None

    def tablero_lleno(self):
        for fila in self.tablero:
            if " " in fila:
                return False

        return True

    def reiniciar(self):
        self.tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        if random.randint(1, 2) == 1:
            self.jugador_actual = self.nacho
            self.simbolo_actual = "X"
        else:
            self.jugador_actual = self.esqueleto
            self.simbolo_actual = "O"

        self.juego_activo = True

    def cambiar_turno(self):
        if self.jugador_actual == self.nacho:
            self.jugador_actual = self.esqueleto
            self.simbolo_actual = "O"
        else:
            self.jugador_actual = self.nacho
            self.simbolo_actual = "X"


historial = {}

print("=== TRES EN RAYA DEL MONASTERIO ===")

while True:
    print("\n1. Entrar al ring")
    print("2. Ver gloria")
    print("3. Salir del monasterio")

    opcion = input("Elige una opcion: ")

    while opcion not in ["1", "2", "3"]:
        opcion = input("Opcion invalida luchador: ")

    if opcion == "1":
        nacho = input("Nombre del luchador 1: ")
        esqueleto = input("Nombre del luchador 2: ")

        if nacho not in historial:
            historial[nacho] = 0

        if esqueleto not in historial:
            historial[esqueleto] = 0

        juego = TresEnRaya(nacho, esqueleto)

        print("\nComienza:", juego.jugador_actual)

        while juego.juego_activo:
            juego.mostrar_tablero()

            while True:
                try:
                    posicion = int(input(f"\n{juego.jugador_actual} ({juego.simbolo_actual}) elige posicion (1-9): "))

                    if juego.colocar_ficha(posicion):
                        break

                except:
                    print("Pon un numero valido luchador.")

            ganador = juego.verificar_ganador()

            if ganador != None:
                juego.mostrar_tablero(False)

                print(f"\n{juego.jugador_actual.upper()} TIENE LAS EAGLE POWERS!")

                historial[juego.jugador_actual] += 1

                juego.juego_activo = False

            elif juego.tablero_lleno():
                juego.mostrar_tablero(False)

                print("\nEMPATE DE MACHOS!")

                juego.juego_activo = False

            else:
                juego.cambiar_turno()

        print("\nGLORIA ACTUAL:")
        print(historial)

    elif opcion == "2":
        print("\nGLORIA DE LOS LUCHADORES")
        print(historial)

    elif opcion == "3":
        print("\nHasta luego luchador.")
        break
