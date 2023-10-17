# 4. (Parcial 2021) Venta de Cruceros
# Una empresa que vende cruceros, desea un programa para administrar la información de venta de pasajes.
# Por cada pasaje se conoce: pasaporte del pasajero (cadena de caracteres), nombre completo, código de destino
# (100: Bahamas, 101: Bermudas: 102: Puerto Rico, 103: República Dominicana), código de clase (un número entero
# entre 1 y 10, por ejemplo: 1: Clase Preferencial, 2: Clase superior, 3: Clase Turista, etc.) y el monto abonado
# por el pasaje. Se desea almacenar la información referida a los n pasajes en un arreglo de registros de tipo Pasaje
# (definir el tipo Pasaje y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de los n pasajes. Valide que el destino y el código de clase se encuentren
# en el rango correcto. Puede hacer la carga en forma manual, o puede generar los datos en forma automática
# (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
#
# 2- Mostrar los datos de todos los pasajes emitidos ordenados de mayor a menor de acuerdo al monto abonado por
# el pasaje. Los pasajes deben mostrarse a razón de uno por línea y mostrando el nombre del destino en lugar de sus códigos.
#
# 3- Determine la recaudación acumulada para cada una de las 10 clases posibles (un acumulador por cada clase).
# Muestre los resultados que sean mayores a cero, y determina y muestre la clase con mayor recaudación (aquella
# clase cuyo monto acumulado de ventas es el mayor entre las 10 clases).
#
# 4- Mostrar todos los pasajes vendidos que correspondan a la clase 3, cuyo monto sea superior al monto promedio
# pagado en esa clase.
#
# 5- Buscar un pasajero por pasaporte. Si se encuentra,  mostrar el mensaje "Pasajero <Nombre>, por favor
# concurrir a atención al cliente". Si no se encuentra indicar la situación con un mensaje. Si existe más de un
# registro que coincida con el mismo pasaporte, debe mostrar sólo el primero que encuentre.

import random
from pasajes import *

DESTINOS = {100: "Bahamas", 101: "Bermudas", 102: "Puerto Rico", 103: "República Dominicana"}

def menu():
    print("menu de opciones")
    print("1) Cargar arreglo")
    print("2) Mostrar los datos de todos los pasajes emitidos ordenados de mayor a menor de acuerdo al monto abonado por el pasaje")
    print("3) recaudación acumulada para cada una de las 10 clases posibles")
    print("4) Mostrar todos los pasajes vendidos que correspondan a la clase 3, cuyo monto sea superior al monto promedio pagado en esa clase.")
    print("5) Buscar un pasajero por pasaporte")
    print("0) Salir")
    opcion = int(input("Elija una opcion: "))
    return opcion


def cargar_arreglo(arreglo_pasajes, n):
    NOMBRES = ("Adrian", "Lucas", "Mario", "Gustavo", "Gloria", "Camila", "Lorena")

    pasaporte = random.randint(10_000_000, 40_000_000)
    nombre = random.choice(NOMBRES)
    destino = validar_entre(100,103, "Introduzca codigo de destino (entre 100 y 103): ")
    clase = validar_entre(1,10, "Introduzca codigo de clase (entre 1 y 10): ")
    monto = random.randint(20000, 120000)

    nuevo_pasaje = Pasaje(pasaporte, nombre, destino, clase, monto)

    arreglo_pasajes.append(nuevo_pasaje)

def carga_aleatoria (arreglo_pasajes, n):
    NOMBRES = ("Adrian", "Lucas", "Mario", "Gustavo", "Gloria", "Camila", "Lorena")

    for i in range(n):
        pasaporte = random.randint(10_000_000, 40_000_000)
        nombre = random.choice(NOMBRES)
        destino = random.randint(100, 103)
        clase = random.randint(1, 10)
        monto = random.randint(20000, 120000)
        nuevo_pasaje = Pasaje(pasaporte, nombre, destino, clase, monto)

        arreglo_pasajes.append(nuevo_pasaje)



def validar_entre(lim_inf, lim_sup, mensaje):
    numero = lim_inf - 1
    while numero < lim_inf or numero > lim_sup:
        numero = int(input(mensaje))
        if numero < lim_inf or numero > lim_sup:
            print(f"ERROR! el numero debe estar entre {lim_inf} y {lim_sup}")
    return numero


def ordenar(arreglo_pasajes):
    n = len(arreglo_pasajes)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo_pasajes[i].monto < arreglo_pasajes[j].monto:
                arreglo_pasajes[i], arreglo_pasajes[j] = arreglo_pasajes[j], arreglo_pasajes[i]


def recaudacion_acumulada(arreglo_pasajes):
    recaudacion = 10 * [0]
    n = len(arreglo_pasajes)
    for i in range(n):
        posicion = arreglo_pasajes[i].clase - 1
        recaudacion[posicion] += arreglo_pasajes[i].monto
    return recaudacion


def mayor(recaudacion):
    mayor = 0
    posicion = -1
    for i in range(len(recaudacion)):
        if recaudacion[i] > mayor:
            mayor = recaudacion[i]
            posicion = i
    return mayor, posicion

# 4- Mostrar todos los pasajes vendidos que correspondan a la clase 3, cuyo monto sea superior al monto promedio
# pagado en esa clase.
def monto_promedio_clase(arreglo_pasajes, clase):
    n = len(arreglo_pasajes)
    contador = 0
    acum = 0
    for i in range(n):
        if arreglo_pasajes[i].clase == clase:
            contador += 1
            acum += arreglo_pasajes[i].monto
    if contador > 0:
        return round(acum/contador, 2)
    else:
        return 0

# 5- Buscar un pasajero por pasaporte. Si se encuentra,  mostrar el mensaje "Pasajero <Nombre>, por favor
# concurrir a atención al cliente". Si no se encuentra indicar la situación con un mensaje. Si existe más de un
# registro que coincida con el mismo pasaporte, debe mostrar sólo el primero que encuentre.
def buscar_pasajero(arreglo_pasajes, pasaporte_buscado):
    n = len(arreglo_pasajes)
    for i in range(n):
        if arreglo_pasajes[i].pasaporte == pasaporte_buscado:
            return arreglo_pasajes[i]
    return -1


def principal():
    arreglo_pasajes = []
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = int(input("Ingrese cantidad de pasajes a cargar: "))
            carga_aleatoria(arreglo_pasajes, n)

        # 2- Mostrar los datos de todos los pasajes emitidos ordenados de mayor a menor de acuerdo al monto abonado por
        # el pasaje. Los pasajes deben mostrarse a razón de uno por línea y mostrando el nombre del destino en lugar de sus códigos.
        if opcion == 2:
            ordenar(arreglo_pasajes)
            for i in range(len(arreglo_pasajes)):
                print(arreglo_pasajes[i])

        # 3- Determine la recaudación acumulada para cada una de las 10 clases posibles (un acumulador por cada clase).
        # Muestre los resultados que sean mayores a cero, y determina y muestre la clase con mayor recaudación (aquella
        # clase cuyo monto acumulado de ventas es el mayor entre las 10 clases).
        if opcion == 3:
            recaudacion = recaudacion_acumulada(arreglo_pasajes)
            mayor_recaudacion, posicion = mayor(recaudacion)

            for i in range(len(recaudacion)):
                if recaudacion[i] > 0:
                    print(f"La recaudacion de la clase {i+1} fue de: ${recaudacion[i]}")

            print(f"La mayor recaudacion fue de ${mayor_recaudacion} y fue computada por la clase {posicion+1}")

        # 4- Mostrar todos los pasajes vendidos que correspondan a la clase 3, cuyo monto sea superior al monto promedio
        # pagado en esa clase.
        if opcion == 4:
            promedio = monto_promedio_clase(arreglo_pasajes, 3)
            for i in range(n):
                if arreglo_pasajes[i].monto > promedio and arreglo_pasajes[i].clase == 3:
                    print(arreglo_pasajes[i])
            print(f"El monto promedio para la clase es: {promedio}")

        # 5- Buscar un pasajero por pasaporte. Si se encuentra,  mostrar el mensaje "Pasajero <Nombre>, por favor
        # concurrir a atención al cliente". Si no se encuentra indicar la situación con un mensaje. Si existe más de un
        # registro que coincida con el mismo pasaporte, debe mostrar sólo el primero que encuentre.
        if opcion == 5:
            pasaporte_buscado = int(input("Introduzca numero de pasaporte buscado: "))
            pasajero_buscado = buscar_pasajero(arreglo_pasajes, pasaporte_buscado)
            if pasajero_buscado != -1:
                print(f"Pasajero {pasajero_buscado.nombre}, por favor concurrir a atención al cliente ")
            else:
                print("NO se encontró el pasajero")


if __name__ == '__main__':
    principal()