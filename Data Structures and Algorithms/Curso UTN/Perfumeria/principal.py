# Una perfumería desea un programa que procese los datos de las ventas que realiza. En cada Venta
# se registran los siguientes datos: el número de factura, importe de la factura, el tipo de factura
# (A, B, C o E), el apellido de la persona que realiza la compra, y el tipo del perfume vendido
# (un número entero para indicar su marca, entre 1 y 17, por ejemplo: 1: Chanel, 2: Paco Rabanne, etc.).
# Se desea almacenar la información referida a las ventas que realiza la perfumería en un arreglo de
# registros de tipo Venta (definir el tipo Venta y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de n ventas realizadas. Valide que el importe de la factura sea
# mayor a 0 y menor a 200000. Valide que el tipo de factura sea alguno de los tipos válidos: A, B, C o E, y
# valide también que el tipo de perfume sea un número entero entre 1 y 17 ambos incluidos. Puede hacer la carga
# en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de
# ambas técnicas si lo desea. Pero al menos una debe programar.
#
# 2- Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de la factura sea
# distinto de t (x y t son valores que se cargan por teclado). El listado debe salir ordenado de mayor a menor
# según los apellidos de las personas que realizaron la compra.
#
# 3- Determinar y mostrar el importe total facturado para cada uno de los 17 tipos posibles pero informe por
# pantalla solamente el total facturado correspondiente al tipo de perfume z (cargar el número z por teclado).
#
# 4- Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de
# perfume se encuentre entre 5 y 12 y que no sean con factura de tipo C. Si no existe ninguna venta que cumpla
# con ese criterio informarlo por pantalla.
#
# 5- Determinar si existe una venta cuyo número de factura sea igual a n (cargar n por teclado) y cuyo importe
# de factura sea menor a a un valor p que se carga por teclado. Si existe, mostrar sus datos. Si no existe,
# informar con un mensaje.

import random
from ventas import *

def menu():
    print("Menu de opciones")
    print("1) Cargar el arreglo pedido con los datos de n ventas realizadas.")
    print("2) Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de "
          "la factura sea distinto de t")
    print("3) Determinar y mostrar el importe total facturado para cada uno de los 17 tipos")
    print("4) Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de "
          "perfume se encuentre entre 5 y 12 y que no sean con factura de tipo C")
    print("5) Determinar si existe una venta cuyo número de factura sea igual a n y cuyo importe de factura"
          " sea menor a a un valor p que se carga por teclado")
    print("0) Salir")
    opcion = int(input("Elija una de las opciones:"))

    return opcion

def validar_entre(lim_inf, lim_sup, mensaje):
    numero = lim_inf - 1
    while numero <= lim_inf or numero >= lim_sup:
        numero = int(input(mensaje))
        if numero <= lim_inf or numero >= lim_sup:
            print(f"ERROR! El numero debe estar entre {lim_inf} y {lim_sup}.")
    return numero

def validar_letra(lista_letras, mensaje):
    letra = "z"
    while letra not in lista_letras:
        letra = input(mensaje)
        if letra not in lista_letras:
            print (f"ERROR! Las letras posibles deben ser culquiera de las siguientes {lista_letras}")
    return letra


def cargar_arreglo(arreglo_ventas, n):# mayor a 0 y menor a 200000
    apellidos = ["Parodi", "Baez", "Ramirez", "Milei", "Fernandez", "Messi", "Mc Alistar"]
    for i in range(n):
        número_factura = validar_entre(0, 200000, "Ingrese numero de factura (mayor a cero y menor a 200000: ")
        importe_factura = round(random.uniform(50, 450), 2)
        tipo_factura = validar_letra("ABCE", "Ingrese tipo de factura A,B,C o E:")
        apellido_comprador = random.choice(apellidos)
        tipo_perfume = validar_entre(0, 18, "Ingrese numero de perfume entre 1 y 17: ")
        nueva_venta = Venta(número_factura, importe_factura, tipo_factura, apellido_comprador, tipo_perfume)

        arreglo_ventas.append(nueva_venta)


def carga_aleatoria(arreglo_ventas, n):# mayor a 0 y menor a 200000
    apellidos = ["Parodi", "Baez", "Ramirez", "Milei", "Fernandez", "Messi", "Mc Alistar"]
    for i in range(n):
        número_factura = random.randint(1, 199999)
        importe_factura = round(random.uniform(50, 450), 2)
        tipo_factura = random.choice("ABCE")
        apellido_comprador = random.choice(apellidos)
        tipo_perfume = random.randint(1, 17)
        nueva_venta = Venta(número_factura, importe_factura, tipo_factura, apellido_comprador, tipo_perfume)

        arreglo_ventas.append(nueva_venta)


def ordenar_arreglo(arreglo_ventas):
    n = len(arreglo_ventas)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo_ventas[i].apellido < arreglo_ventas[j].apellido:
                arreglo_ventas[i], arreglo_ventas[j] = arreglo_ventas[j], arreglo_ventas[i]


def filtrar2(arreglo_ventas, t, x):
    # Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de la factura sea distinto de t
    arreglo_filtrado = []
    n = len(arreglo_ventas)
    for i in range(n):
        if arreglo_ventas[i].importe > x and arreglo_ventas[i].tipo_factura == t:
            arreglo_filtrado.append(arreglo_ventas[i])
    return arreglo_filtrado

def filtrar4(arreglo_ventas):
    # Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de la factura sea distinto de t
    arreglo_filtrado = []
    n = len(arreglo_ventas)
    for i in range(n):
        if arreglo_ventas[i].tipo_factura == "C" and (5 <= arreglo_ventas[i].tipo_perfume <= 12):
            arreglo_filtrado.append(arreglo_ventas[i])
    return arreglo_filtrado

def total_tipo_perfume(arreglo_ventas):
    acumuladores = 17 * [0]
    n = len(arreglo_ventas)
    for i in range(n):
        posicion = arreglo_ventas[i].tipo_perfume - 1
        acumuladores[posicion] += arreglo_ventas[i].importe
    return acumuladores


def buscar_factura(arreglo_ventas, n, p):
    largo = len(arreglo_ventas)
    # n (cargar n por teclado) y cuyo importe de factura sea menor a a un valor p que se carga por teclado
    for i in range(largo):
        if arreglo_ventas[i].numero_factura == n and arreglo_ventas[i].importe < p:
            return i
    return -1


def principal():
    opcion = -1
    arreglo_ventas = []
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = int(input("Ingrese cantidad de datos de ventas a cargar: "))
            carga_aleatoria(arreglo_ventas, n)

        if opcion == 2:
            ordenar_arreglo(arreglo_ventas)
            x = int(input("Ingrese importe de la factura: "))
            t = input("Ingrese tipo de factura A, B, C o E: ")
            arreglo_filtrado = filtrar2(arreglo_ventas, t, x)
            for i in range(len(arreglo_ventas)):
                print(arreglo_ventas[i])
            print("\n Arreglo filtrado:")
            for i in range(len(arreglo_filtrado)):
                print(arreglo_filtrado[i])
        if opcion == 3:
            importes_por_tipo = total_tipo_perfume(arreglo_ventas)
            print(f"Importes por tipo: {importes_por_tipo}")
            z = int(input("Ingrese el tipo de perfume del cual desea ver el monto total: "))
            print(f"El importe total del perfume tipo {z} es de: ${importes_por_tipo[z]}")
        if opcion == 4:
            # 4- Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de
            # perfume se encuentre entre 5 y 12 y que no sean con factura de tipo C. Si no existe ninguna venta que cumpla
            # con ese criterio informarlo por pantalla.
            arreglo_perfumes_factura = filtrar4(arreglo_ventas)
            largo = len(arreglo_perfumes_factura)
            if largo != 0:
                for i in range(largo):
                    print(f"Numero: {arreglo_perfumes_factura[i].numero_factura}, Comprador: {arreglo_perfumes_factura[i].apellido}"
                          f", Importe: ${arreglo_perfumes_factura[i].importe}")
            else:
                print("No se encontraron elementos que cumplas las especificaciones")

        if opcion == 5:
            # 5- Determinar si existe una venta cuyo número de factura sea igual a n (cargar n por teclado) y cuyo importe
            # de factura sea menor a un valor p que se carga por teclado. Si existe, mostrar sus datos. Si no existe,
            # informar con un mensaje.
            n = int(input("Ingresar numero de factura: "))
            p = int(input("Ingresar importe: "))
            posicion = buscar_factura(arreglo_ventas, n, p)
            if posicion != -1:
                print("Se encontró el ticket. Sus datos son")
                print(arreglo_ventas[posicion])
            else:
                print("No se encontró ticket que cumpla con el criterio solicitado")


if __name__ == '__main__':
    principal()