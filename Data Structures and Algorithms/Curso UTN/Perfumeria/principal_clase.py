# 3. (Parcial 2021) - La Perfumeria
# Una perfumería desea un programa que procese los datos de las ventas que realiza. En cada Venta se registran
# los siguientes datos: el número de factura, importe de la factura, el tipo de factura (A, B, C o E), el apellido
# de la persona que realiza la compra, y el tipo del perfume vendido (un número entero para indicar su marca,
# entre 1 y 17, por ejemplo: 1: Chanel, 2: Paco Rabanne, etc.). Se desea almacenar la información referida a las
# ventas que realiza la perfumería en un arreglo de registros de tipo Venta (definir el tipo Venta y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de n ventas realizadas. Valide que el importe de la factura sea mayor
# a 0 y menor a 200000. Valide que el tipo de factura sea alguno de los tipos válidos: A, B, C o E, y valide también
# que el tipo de perfume sea un número entero entre 1 y 17 ambos incluidos. Puede hacer la carga en forma manual,
# o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si
# lo desea. Pero al menos una debe programar.
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
from venta_en_clase import *


def menu():
    print("menu de opciones")
    print("Opcion 1")
    print("Opcion 2")
    print("Opcion 3")
    print("Opcion 4")
    print("Opcion 5")
    print("Opcion 0: Salir")
    opcion = int(input("Elija una de las opciones: "))
    return opcion


def cargar_arreglo(arreglo_ventas, n):
    APELLIDOS = ["parodi", "baez", "saavedra", "jacinto"]
    for i in range(n):
        numero = validar_entre(0, 200_000, "Ingrese numero entre 1 y 199999")
        importe = random.randint(25000, 85000)
        factura = random.choice("ABCE")
        apellido = random.choice(APELLIDOS)
        tipo_perfume = random.randint(1, 17)
        nueva_venta = Venta(numero, importe, factura, apellido, tipo_perfume)
        arreglo_ventas.append(nueva_venta)


def carga_aleatoria(arreglo_ventas, n):
    APELLIDOS = ["parodi", "baez", "saavedra", "jacinto"]
    for i in range(n):
        numero = random.randint(1, 199_999)
        importe = random.randint(25000, 85000)
        factura = random.choice("ABCE")
        apellido = random.choice(APELLIDOS)
        tipo_perfume = random.randint(1, 17)
        nueva_venta = Venta(numero, importe, factura, apellido, tipo_perfume)
        arreglo_ventas.append(nueva_venta)


def validar_entre(li, ls, mensaje):
    numero = li - 1
    while numero <= li or numero >= ls:
        numero = int(input(mensaje))
        if numero <= li or numero >= ls:
            print(f"ERROR! El numero debe estar entre {li} y {ls}")
    return numero


def ordenar(arreglo_ventas):
    n = len(arreglo_ventas)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo_ventas[i].apellido < arreglo_ventas[j].apellido:
                arreglo_ventas[i], arreglo_ventas[j] = arreglo_ventas[j], arreglo_ventas[i]


def listar(arreglo_ventas, t, x):
    n = len(arreglo_ventas)
    for venta in arreglo_ventas:
        if venta.importe > x and venta.factura != t:
            print(venta)


def sumar_importe_tipo(arreglo_ventas):
    importe_por_tipo = 17 * [0]
    for venta in arreglo_ventas:
        importe_por_tipo[venta.tipo_perfume -1] += venta.importe
    return importe_por_tipo


def listar_2(arreglo_ventas):
    encontrado = False
    for venta in arreglo_ventas:
        if 5 <= venta.tipo_perfume <= 12 and venta.factura != "C":
            print(venta)
            encontrado = True
    if not encontrado:
        print("No se encontró lo buscado")


def buscar(arreglo_ventas, n, p):
    for venta in arreglo_ventas:
        if venta.numero == n and venta.importe < p:
            return venta


def principal():
    arreglo_ventas = []
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = int(input("Ingrese cantidad de elementos del arreglo: "))
            carga_aleatoria(arreglo_ventas, n)

        if opcion == 2:
            ordenar(arreglo_ventas)
            t = "A"
            x = 35000
            listar(arreglo_ventas, t, x)

        if opcion == 3:
            importes_por_tipo = sumar_importe_tipo(arreglo_ventas)
            z = int(input("Ingrese el tipo de perfume para ver la facturacion total: "))
            print(f"El importe del perfume tipo {z} es: ${importes_por_tipo[z-1]}")

        if opcion == 4:
            listar_2(arreglo_ventas)

        if opcion == 5:
            numero = int(input("cargar numero de factura: "))
            p = int(input("Ingrese importe: "))
            encontrado = buscar(arreglo_ventas, numero, p)
            print(encontrado if encontrado else "no se encontró lo buscado")

    print("Proceso terminado. Gracias")


if __name__ == '__main__':
    principal()