# 4. (Parcial 2021) Venta de Cruceros
# Una empresa que vende cruceros, desea un programa para administrar la información de venta de pasajes.
# Por cada pasaje se conoce: pasaporte del pasajero (cadena de caracteres), nombre completo, código de destino
# (100: Bahamas, 101: Bermudas: 102: Puerto Rico, 103: República Dominicana), código de clase (un número entero
# entre 1 y 10, por ejemplo: 1: Clase Preferencial, 2: Clase superior, 3: Clase Turista, etc.) y el monto abonado
# por el pasaje. Se desea almacenar la información referida a los n pasajes en un arreglo de registros de tipo
# Pasaje (definir el tipo Pasaje y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de los n pasajes. Valide que el destino y el código de clase se
# encuentren en el rango correcto. Puede hacer la carga en forma manual, o puede generar los datos en forma
# automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
#
# 2- Mostrar los datos de todos los pasajes emitidos ordenados de mayor a menor de acuerdo al monto abonado por
# el pasaje. Los pasajes deben mostrarse a razón de uno por línea y mostrando el nombre del destino en lugar de
# sus códigos.
#
# 3- Determine la recaudación acumulada para cada una de las 10 clases posibles (un acumulador por cada clase).
# Muestre los resultados que sean mayores a cero, y determina y muestre la clase con mayor recaudación
# (aquella clase cuyo monto acumulado de ventas es el mayor entre las 10 clases).
#
# 4- Mostrar todos los pasajes vendidos que correspondan a la clase 3, cuyo monto sea superior al monto
# promedio pagado en esa clase.
#
# 5- Buscar un pasajero por pasaporte. Si se encuentra,  mostrar el mensaje "Pasajero <Nombre>, por favor
# concurrir a atención al cliente". Si no se encuentra indicar la situación con un mensaje. Si existe más
# de un registro que coincida con el mismo pasaporte, debe mostrar sólo el primero que encuentre.


import random
from pasajes2 import *

def menu():
    print("menu")
    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4")
    print("opcion 5")
    opcion = int(input("Elija una opcion: "))
    return opcion

def carga_aleatoria(n):
    nombres = ["parodi", "piparo", "falletti", "piccioni", "barreda", "videla"]
    arreglo_ventas = []
    for i in range(n):
        pasaporte = random.randint(10_000_000, 20_000_000)
        nombre = random.choice(nombres)
        cod_destino = random.randint(100, 103)
        cod_clase = random.randint(1,10)
        monto = random.randint(25000,150000)
        nueva_venta = Pasaje(pasaporte, nombre, cod_destino, cod_clase, monto)
        arreglo_ventas.append(nueva_venta)
    return arreglo_ventas


def validar_entre(li, ls, mensaje):
    numero = li - 1
    while numero <= li or numero >= ls:
        numero = int(input(mensaje))
        if numero <= li or numero >= ls:
            print(f"ERROR! el numero debe estar entre {li} y {ls}")
    return numero

def ordenar(arreglo_ventas):
    n = len(arreglo_ventas)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo_ventas[i].monto < arreglo_ventas[j].monto:
                arreglo_ventas[i], arreglo_ventas[j] = arreglo_ventas[j], arreglo_ventas[i]


def recaudacion_acumulada(arreglo_ventas):
    recaudaciones = 10 * [0]
    for venta in arreglo_ventas:
        recaudaciones[venta.cod_clase - 1] += venta.monto
    return recaudaciones


def promedio(arreglo_ventas):
    acum = contador = 0
    for venta in arreglo_ventas:
        if venta.cod_clase == 3:
            acum += venta.monto
            contador += 1
    if contador > 0:
        return acum / contador
    else:
        return 0


def listar4(arreglo_ventas, valor_promedio):
    for venta in arreglo_ventas:
        if venta.cod_clase == 3 and venta.monto > valor_promedio:
            print(venta)


def buscar_pasajero(arreglo_ventas, pasaporte):
    for venta in arreglo_ventas:
        if venta.pasaporte == pasaporte:
            return venta


def principal():
    opcion = -1

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = int(input("Ingrese cantidad de datos a generar: "))
            arreglo_ventas = carga_aleatoria(n)
        if opcion == 2:
            ordenar(arreglo_ventas)
            for venta in arreglo_ventas:
                print(venta)

        if opcion == 3:
            recaudacion_clase = recaudacion_acumulada(arreglo_ventas)
            for i in range(len(recaudacion_clase)):
                if recaudacion_clase[i] > 0:
                    print(f"Recaudacion {i+1} es de: ${recaudacion_clase[i]}")

        if opcion == 4:
            promedio_ventas_clase3 = promedio(arreglo_ventas)
            print(f"El monto promedio de la clase 3 es ${promedio_ventas_clase3}. Los registros que superan dicho valor son:")
            listar4(arreglo_ventas, promedio_ventas_clase3)

        if opcion == 5:
            pasaporte = int(input("Introduzca numero de pasaporte: "))
            encontrado = buscar_pasajero(arreglo_ventas, pasaporte)
            print(f"Pasajero {encontrado.nombre} por favor conccurrir a atencion al cliente" if encontrado else f"NO se encontró el pasajero")
    print("Proceso concluido. Gracias!")





if __name__ == '__main__':
    principal()