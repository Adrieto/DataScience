"""Desarrollar un programa para implementar un juego de cartas de la baraja española.
Es una competencia de n rondas entre 2 jugadores (n se carga por teclado, validar)

En cada ronda, cada jugador recibe una carta (cuyo número y palo el programa deberá generar de forma aleatoria)
y se define la ronda de la siguiente manera:

*El jugador que tenga la carta de mayor valor, se lleva ambas.
*Si las cartas son del mismo valor, se las lleva quien tenga una carta de oro.
*Si ambos tienen oro o ninguno lo tiene, cada jugador recupera su carta.

Los puntos de cada jugador se determinan sumando los valores de todas las cartas que ganó.
Será triunfador el que tenga mayor puntaje total.
"""
import random

def generador():
    numero = range(1, 13)
    palo = range(4)  # 0:Oro, 1:Basto, 2:Copa, 3: Espada

    n = random.choice(numero)
    p = random.choice(palo)
    return n, p


def gana (n1, p1, n2, p2, puntos1, puntos2):
    if n1 > n2:
        ganador = 1
        puntos1 += n1
    elif n2 > n1:
        ganador = 2
        puntos2 += n2

    else: # Empate
        if p1 == 0 and p2 != 0:
            ganador = 1
            puntos1 += n1
        elif p1 != 0 and p2 == 0:
            ganador = 2
            puntos2 += n2
        else:
            ganador = None

    return ganador, puntos1, puntos2

corte = input ("si quiere jugar otra mano presione enter. Sino ingrese 0:")
puntos_j1 = puntos_j2 = 0

while corte == "":
    # Jugador 1:
    n1,p1 = generador()
    # Jugador 2:
    n2,p2 = generador()

    palo = ("Oro", "Basto", "Copa", "Espada")

    #Mostramos cartas:
    print (f"El jugador 1 recibió un {n1} de {palo[p1]}")
    print (f"El jugador 2 recibió un {n2} de {palo[p2]}")

    #Determinamos el ganador:
    ganador, puntos_j1, puntos_j2 = gana(n1,p1,n2,p2, puntos_j1, puntos_j2)

    #Mostramos el resultado de la ronda:
    if ganador != None:
        print (f"Ganó el jugador {ganador}! acumula {puntos_j1 if ganador == 1 else puntos_j2} puntos")
    else:
        print(f"Ronda empatada")

    corte = input("Otra ronda? presione enter. Sino ingrese cualquier cosa.")

# Mostramos los resultados finales
print()
print(f"Puntos totales jugador 1: {puntos_j1}")
print(f"Puntos totales jugador 2: {puntos_j2}")
if puntos_j1 > puntos_j2:
    print(f"Ganó el jugador 1 con {puntos_j1} puntos. El jugador 2 sacó {puntos_j2} puntos" )
elif puntos_j1 < puntos_j2:
    print(f"Ganó el jugador 2 con {puntos_j2} puntos. El jugador 1 sacó {puntos_j1} puntos" )
else:
    print(f"Empate con {puntos_j1} y {puntos_j2} puntos para ambos jugadores")












