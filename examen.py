import random
import os

class Conecta4:
    def __init__(self, nacho, esqueleto):
        self.nacho = nacho
        self.esqueleto = esqueleto

        self.tablero = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]

        if random.randint(1, 2) == 1:
            self.jugador_actual = nacho
            self.simbolo_actual = "X"
        else:
            self.jugador_actual = esqueleto
            self.simbolo_actual = "O"

        self.juego_activo = True

    def mostrar_tablero(self, con_columnas=True):
        if con_columnas:
            print(" 1 2 3 4 5")

        for fila in self.tablero:
            print("+-+-+-+-+-+")
            print("|" + "|".join(fila) + "|")

        print("+-+-+-+-+-+")

    def soltar_ficha(self, columna):
        columna = columna - 1

        if columna < 0 or columna > 4:
            print("Esa columna no existe en el ring.")
            return False

        for fila in range(3, -1, -1):
            if self.tablero[fila][columna] == " ":
                self.tablero[fila][columna] = self.simbolo_actual
                return True

        print("La columna ya esta llena de poder.")
        return False

    def verificar_ganador(self):
        for fila in self.tablero:
            for i in range(2):
                if fila[i] != " ":
                    if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                        return fila[i]

        return None

    def tablero_lleno(self):
        for fila in self.tablero:
            if " " in fila:
                return False

        return True

    def reiniciar(self):
        self.tablero = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
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


def cargar_puntuaciones():
    puntuaciones = {}

    if os.path.exists("puntuaciones.txt"):
        archivo = open("puntuaciones.txt", "r")

        for linea in archivo:
            datos = linea.strip().split(",")

            nombre = datos[0]
            victorias = int(datos[1])

            puntuaciones[nombre] = victorias

        archivo.close()

    return puntuaciones


def guardar_puntuaciones(puntuaciones):
    archivo = open("puntuaciones.txt", "w")

    for nombre in puntuaciones:
        archivo.write(nombre + "," + str(puntuaciones[nombre]) + "\n")

    archivo.close()


print("=== CONECTA 4 DEL MONASTERIO ===")
print("Cargando gloria de los luchadores...")

puntuaciones = cargar_puntuaciones()

while True:
    print("\n1. Entrar al ring")
    print("2. Ver gloria de los luchadores")
    print("3. Abandonar el monasterio")

    opcion = input("Elige una opcion: ")

    while opcion not in ["1", "2", "3"]:
        opcion = input("Opcion invalida. Elige 1, 2 o 3: ")

    if opcion == "1":
        nacho = input("Nombre del luchador 1: ")
        esqueleto = input("Nombre del luchador 2: ")

        if nacho not in puntuaciones:
            puntuaciones[nacho] = 0

        if esqueleto not in puntuaciones:
            puntuaciones[esqueleto] = 0

        juego = Conecta4(nacho, esqueleto)

        print("\nComienza:", juego.jugador_actual)

        while juego.juego_activo:
            juego.mostrar_tablero()

            while True:
                try:
                    columna = int(input(f"{juego.jugador_actual} ({juego.simbolo_actual}) elige columna: "))

                    if juego.soltar_ficha(columna):
                        break

                except:
                    print("Pon un numero valido luchador.")

            ganador = juego.verificar_ganador()

            if ganador != None:
                juego.mostrar_tablero()

                print(f"\n{juego.jugador_actual.upper()} TIENE LAS EAGLE POWERS!")

                puntuaciones[juego.jugador_actual] += 1

                juego.juego_activo = False

            elif juego.tablero_lleno():
                juego.mostrar_tablero()

                print("\nEMPATE DE MACHOS!")

                juego.juego_activo = False

            else:
                juego.cambiar_turno()

        print("\nPUNTUACIONES:")
        print(puntuaciones)

        otra = input("\nQuieres otra batalla? (s/n): ")

        while otra.lower() not in ["s", "n"]:
            otra = input("Pon s o n luchador: ")

        if otra.lower() == "s":
            juego.reiniciar()
        else:
            print("\nGuardando gloria...")
            guardar_puntuaciones(puntuaciones)
            print("Hasta luego luchador.")
            break

    elif opcion == "2":
        print("\nGLORIA DE LOS LUCHADORES")
        print(puntuaciones)

    elif opcion == "3":
        print("\nGuardando gloria...")
        guardar_puntuaciones(puntuaciones)
        print("Hasta luego luchador.")
        break