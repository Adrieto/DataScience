# 3. Pagos Regalías
# Una empresa dedicada al cobro de regalias de la industria audiovisual no ha solicitado un programa que permita cargar
# los pagos que le debe realizar a sus clientes. Para ellos se sabe que un pago esta conformado por la siguiente información:
#   * Numero (string)
#   * Nombre del cliente (string)
#   * Tipo de Empleo (0 - Director, 1 - Productor, 2 - Maquillador, 3 - Actor, 4 - Asistentes, 5 - Especialista CGI, 6 - Vestuarista)
#   * Tipo de Producto (1 - Pelicula, 2 - Serie, 3 - Documental, 4 - Videojuego, 5 - Corto Animación)
#   * Monto a Pagar (float)
#   * Gastos a Cobrar (float)
#
# Se sabe que toda la información se encuentra en un archivo llamado pagos.csv, el cual debe ser cargado al iniciar
# el programa. Los registros se deben generar en forma ordenada por el numero del pago. Luego a través de un menú de
# opciones, desarrolle los siguientes puntos:
#
# 1 - Muestre el vector a razón de un registro por línea y a los tipos de empleo y producto con su nombre especificado
#
# 2 - Determine si existe un pago con un numero x pasado por parámetro, si existe incrementar su monto a pagar en
# un 25% y mostrar los datos del registro, si no existe informarlo con un mensaje
#
# 3 - Determinar el neto a pagar por tipo de empleo y tipo de producto (30 contadores en una matriz de acumulación).
# Mostrar solo los netos a pagar para Director, Productor, Maquillador y Actor, de solo los tipos de producto
# Película, Serie o Documental
#
# 4 - Usando la matriz generada, determinar para un tipo de producto x pasado por parámetro cual es el
# total neto a pagar por el mismo.
#
# 5 - Usando el vector, genere un archivo binario con todos los registros cuyo neto a pagar sea mayor al neto
# promedio a pagar y solo si el tipo de producto es una Película o Serie. Muestre el archivo, y al final indicar
# cual es el neto a pagar a todos los clientes
#
# 6 - Usando el vector, buscar un pago perteneciente a un cliente con nombre x pasado por parámetros, si existe
# mostrar sus datos, si no existe generar e insertarlo en el vector
#
# 7 - Salir, grabando previamente el contenido del archivo pagos.csv

import pickle
import io
from pagos import Pago


def insertion_sort(v):
    n = len(v)
    for j in range(1, n):
        k = j - 1
        y = v[j]
        while y < v[k] and k >= 0:
            v[k + 1] = v[k]
            k -= 1
        v[k + 1] = y


def binary_search(arreglo_pagos, valor_buscado):
    n = len(arreglo_pagos)
    izq = 0
    der = n - 1
    while izq <= der:
        medio = (der + izq) // 2
        if arreglo_pagos[medio].numero == valor_buscado:
            pos = medio
            return pos
        elif arreglo_pagos[medio].numero < valor_buscado:
            izq = medio + 1
        elif arreglo_pagos[medio].numero > valor_buscado:
            der = medio - 1
    return -1


def add_in_order(arreglo_pagos, nuevo_pago):
    n = len(arreglo_pagos)
    pos = n
    izq = 0
    der = n - 1
    while izq <= der:
        medio = (der + izq) // 2
        if arreglo_pagos[medio].numero == nuevo_pago.numero:
            pos = medio
            break
        if arreglo_pagos[medio].numero < nuevo_pago.numero:
            izq = medio + 1
        else:
            der = medio - 1
    if izq > der:
        pos = izq
    arreglo_pagos[pos:pos] = [nuevo_pago]


def cargar_arreglo_desde_csv(archivo):
    file = open(archivo)
    lineas = file.readlines()
    lineas = lineas[1::]  # Elimino encabezado
    arreglo_pagos = []

    for linea in lineas:
        numero, nombre, empleo, producto, monto_pagar, gastos_cobrar = linea.strip().split(",")
        nuevo_pago = Pago(numero, nombre, empleo, producto, monto_pagar, gastos_cobrar)
        add_in_order(arreglo_pagos, nuevo_pago)

        #print(nuevo_pago)
    return arreglo_pagos


def mostrar_pagos(arreglo_pagos):
    for pago in arreglo_pagos:
        print(pago)


def netos_a_pagar(arreglo_pagos):
    n = 7  # tipos de empleo
    m = 5  # tipos de producto

    # Creacion de la matriz de contadores
    acumuladores = n * [0]
    for j in range(n):
        acumuladores[j] = [0] * m

    for pago in arreglo_pagos:
        acumuladores[pago.empleo][pago.producto-1] += pago.monto_pagar

    # Redondeo:
    for i in range(n):
        for j in range(m):
            acumuladores[i][j] = round(acumuladores[i][j], 2)

    return acumuladores


# 4 - Usando la matriz generada, determinar para un tipo de producto x pasado por parámetro cual es el
# total neto a pagar por el mismo. (columna)
def total_producto(acumuladores, producto_buscado):
    total_producto_buscado = 0
    for i in range(len(acumuladores)):  # Recorro filas
        total_producto_buscado += acumuladores[i][producto_buscado]
    return total_producto_buscado


def menu():
    print("MENU")
    print("1) Muestre el vector a razón de un registro por línea")
    print("2) Determine si existe un pago con un numero x pasado por parámetro")
    print("3) Determinar el neto a pagar por tipo de empleo y tipo de producto")
    print("4) Usando la matriz generada, determinar para un tipo de producto x cual es el total neto a pagar por el mismo.")
    print("5) Usando el vector, genere un archivo binario con todos los registros cuyo neto a pagar sea mayor al neto promedio a pagar y solo si el tipo de producto es una Película o Serie.")
    print("6) Usando el vector, buscar un pago perteneciente a un cliente con nombre x, si existe mostrar sus datos, si no existe generar e insertarlo en el vector")
    print("7) Salir, grabando previamente el contenido del archivo pagos.csv")
    opcion = int(input("Elija una opcion: "))
    return opcion


def grabar_archivo_binario(arreglo_pagos, promedio):
    archivo = "pagos.dat"
    m = open(archivo, "wb")
    for pago in arreglo_pagos:
        if pago.monto_pagar > promedio:
            pickle.dump(pago, m)
    m.flush()


def calculo_promedio(arreglo_pagos):
    ac = cont = 0
    for pago in arreglo_pagos:
        if 1 <= pago.producto <= 2:
            cont += 1
            ac += pago.monto_pagar
    return ac / cont


def buscar_cliente(arreglo_pagos, x):
    for pago in arreglo_pagos:
        if pago.nombre == x:
            return pago


def grabar_csv(nombre_archivo, arreglo_pagos):
    m = open(nombre_archivo, "w")
    for pago in arreglo_pagos:
        m.write(pago.csv())


def principal():
    archivo = "pagos.csv"
    opcion = -1
    arreglo_pagos = cargar_arreglo_desde_csv(archivo)
    bandera_matriz_creada = False

    while opcion != 7:
        opcion = menu()

        if opcion == 1:
            mostrar_pagos(arreglo_pagos)

        elif opcion == 2:
            nro = input("Ingrese numero de pago a buscar: ")
            pos = binary_search(arreglo_pagos, nro)

            if pos == -1:
                print(f"\t\tNo se encontró el pago numero: {nro}")
            else:
                print(f"\tAntes del cambio: {arreglo_pagos[pos]}")
                arreglo_pagos[pos].monto_pagar = round(1.25 * arreglo_pagos[pos].monto_pagar, 2)
                print(f"\tLuego del cambio: {arreglo_pagos[pos]}")
            #pago_buscado = buscar_pago(arreglo_pagos, nro)

        elif opcion == 3:
            acumuladores = netos_a_pagar(arreglo_pagos)
            bandera_matriz_creada = True
            for i in range(7):
                print(acumuladores[i])
            print("\n Acumuladores requeridos: ")
            print(f"            |  Pelicula  |  Serie  |  Documental ")
            print(f"Director     {acumuladores[0][0:3]}")
            print(f"Productor    {acumuladores[1][0:3]}")
            print(f"Maquillador  {acumuladores[2][0:3]} ")
            print(f"Actor        {acumuladores[3][0:3]}")
        #   * Tipo de Empleo (0 - Director, 1 - Productor, 2 - Maquillador, 3 - Actor, 4 - Asistentes, 5 - Especialista CGI, 6 - Vestuarista)
        #   * Tipo de Producto (1 - Pelicula, 2 - Serie, 3 - Documental, 4 - Videojuego, 5 - Corto Animación)


        elif opcion == 5:
            promedio = calculo_promedio(arreglo_pagos)
            grabar_archivo_binario(arreglo_pagos, promedio)

        elif opcion == 6:
            # Buscar cliente X, si no está, generarlo
            x = input("Introduzca el nombre de la persona a buscar: ")
            cliente_encontrado = buscar_cliente(arreglo_pagos, x)
            if cliente_encontrado:
                print(f"Los datos del cliente son: \n\t{cliente_encontrado}")
            else:  # Creamos el pago
                nuevo_pago = Pago("1Numero12345", x, 3, 3, 4500.00, 1255.25)
                add_in_order(arreglo_pagos, nuevo_pago)

            #  Salir, grabando previamente el contenido del archivo pagos.csv
        elif opcion == 7:
            nombre_archivo = "pagos2.csv"
            grabar_csv(nombre_archivo, arreglo_pagos)


        elif not bandera_matriz_creada:
            print("\tDebe cargarse primero la matriz con la opcion 3")

        # 4 - Usando la matriz generada, determinar para un tipo de producto x pasado por parámetro cual es el
        # total neto a pagar por el mismo.
        elif opcion == 4:
                producto_buscado = int(input("elija el producto buscado (entre 1 y 5)")) - 1
                total_producto_buscado = total_producto(acumuladores, producto_buscado)
                print(f"El total del producto '{producto_buscado+1}' es: ${total_producto_buscado}")


if __name__ == '__main__':
    principal()