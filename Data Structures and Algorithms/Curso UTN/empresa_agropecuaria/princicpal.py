# 2. (Parcial 2021) - Empresa Agropecuaria
# Se pide desarrollar un programa en Python para el enunciado que sigue. El programa obligatoriamente deberá
# plantearse como un proyecto que contenga al menos dos módulos (uno para la definición del tipo de registro
# y las funciones para gestionarlo (a criterio del estudiante) y otro módulo deberá contener el programa
# principal que obligatoriamente debe ser planteado en base a un menú de opciones y con funciones para toda
# situación posible.
#
# Una empresa agropecuaria necesita un programa para procesar los datos de los trabajos ofrecidos.
# Por cada trabajo se tienen los siguientes datos: el número de identificación, la descripción del trabajo,
# el tipo de trabajo (un número entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas,
# 2: cosecha, etc.), el importe a cobrar por ese trabajo y la cantidad de personal afectado al mismo. Se desea
# almacenar la información referida a estos trabajos en un arreglo de registros de tipo Trabajo (definir el tipo
# Trabajo y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:
#
# 1-      Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo
# sea positivo y que el tipo del servicio esté entre 0 y 19. Puede hacer la carga en forma manual, o puede generar
# los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al
# menos una debe programar.
#
# 2-      Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3, en un listado
# ordenado de mayor a menor según los números de identificación de esos trabajos. Al final del listado, mostrar
# además la suma de los importes de todos los registros mostrados.
#
# 3-      Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible de (un contador para
# los trabajos tipo 0, otro para el tipo 1, etc.) En total, 20 contadores. Muestre solo los resultados mayores a cero.
#
# 4-      Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los
# trabajos del arreglo
#
# 5-      Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t,
# siendo num y t dos valores que se cargan por teclado. Si existe, mostrar sus datos. Si no existe, informar
# con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo
# el primero que encuentre.
import random
from empresa import *

def menu():
    print("Menu de opciones")
    print("1) Cargar el arreglo pedido con los datos de los n trabajos")
    print("2) Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3")
    print("3) Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible")
    print("4) Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los trabajos del arreglo")
    print("5) Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t, siendo num y t dos valores que se cargan por teclado")
    print("0) Salir")
    opcion = int(input("Elija una de las opciones"))
    return opcion


def validar_entre(lim_inf, lim_sup, mensaje):
    numero = lim_inf -1
    while numero < lim_inf or numero > lim_sup:
        numero = int(input(mensaje))
        if numero <= lim_inf or numero >= lim_sup:
            print(f"ERROR! El numero debe estar entre {lim_inf} y {lim_sup}")
        else:
            return numero


def validar_mayor_que(limite, mensaje):
    numero = limite
    while numero <= limite :
        numero = int(input(mensaje))
        if numero <= limite:
            print(f"ERROR! El numero debe ser mayor a {limite}")
        else:
            return numero


def cargar_arreglo(arreglo_trabajos, n):
    for i in range(n):
        identificacion = validar_mayor_que(0, "Ingrese el identificador de trabajo (mayor a 0): ")
        descripcion = input("Ingrese la descripcion del trabajo: ")
        tipo_trabajo = validar_entre(0, 19, "Ingrese el tipo de trabajo. Entre 0 y 19: ")
        importe = round(random.uniform(1000,12500), 2)
        personal_afectado = random.randint(2, 10)

        trabajo_nuevo = Trabajo(identificacion, descripcion, tipo_trabajo, importe, personal_afectado)
        arreglo_trabajos.append(trabajo_nuevo)

def cargar_arreglo_aleatorio(arreglo_trabajos, n):
    descripciones = ("Venta", "Compra", "Reparacion", "Envios")
    for i in range(n):
        identificacion = random.randint(1, 100)
        descripcion = random.choice(descripciones)
        tipo_trabajo = random.randint(0, 19)
        importe = round(random.uniform(1000, 12500), 2)
        personal_afectado = random.randint(2, 10)

        trabajo_nuevo = Trabajo(identificacion, descripcion, tipo_trabajo, importe, personal_afectado)
        arreglo_trabajos.append(trabajo_nuevo)

def ordenar(arreglo_trabajos):
    n = len(arreglo_trabajos)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo_trabajos[i].identificacion < arreglo_trabajos[j].identificacion:
                arreglo_trabajos[i], arreglo_trabajos[j] = arreglo_trabajos[j], arreglo_trabajos[i]


def contar_trabajo(arreglo_trabajos):
    n = len(arreglo_trabajos)
    contadores = 20 * [0]
    for i in range(n):
        trabajo = arreglo_trabajos[i].tipo_trabajo
        contadores[trabajo] += 1
    return contadores


def calcular_promedio(arreglo_trabajos):
    acum = 0
    n = len(arreglo_trabajos)
    for i in range(n):
        acum += arreglo_trabajos[i].importe
    promedio = acum/n
    return promedio


# def busqueda_binaria_identificador(arreglo_trabajos, num, tipo_trabajo):
#     n = len(arreglo_trabajos)
#     izq = 0
#     der = n - 1
#
#     while izq <= der:
#         medio = (izq + der) // 2
#         if arreglo_trabajos[medio].identificacion == num and arreglo_trabajos[medio].tipo_trabajo == tipo_trabajo:
#             return medio
#         elif arreglo_trabajos[medio].identificacion < num:
#             izq = medio + 1
#         elif arreglo_trabajos[medio].identificacion > num:
#             der = medio -1
#
#     return -1

def buscar_identificacion_tipo (arreglo_trabajos, num, tipo_trabajo):
    n = len(arreglo_trabajos)
    for i in range(n):
        if arreglo_trabajos[i].identificacion == num and  arreglo_trabajos[i].tipo_trabajo == tipo_trabajo:
            return i
    return -1



def principal():

    opcion = -1
    arreglo_trabajos = []
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = int(input("Ingrese la cantidad de trabajos en el arreglo: "))
            cargar_arreglo_aleatorio(arreglo_trabajos, n)

        # 2-      Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3, en un listado
        # ordenado de mayor a menor según los números de identificación de esos trabajos. Al final del listado, mostrar
        # además la suma de los importes de todos los registros mostrados.
        if opcion == 2:
            ordenar(arreglo_trabajos)
            suma_importes = 0
            for i in range(len(arreglo_trabajos)):
                if arreglo_trabajos[i].personal_afectado > 3:
                    suma_importes += arreglo_trabajos[i].importe
                    print(arreglo_trabajos[i])

            print(f"El importe total acumulado es de: ${round(suma_importes,2)}")

        if opcion == 3:
            # 3-      Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible de (un contador para
            # los trabajos tipo 0, otro para el tipo 1, etc.) En total, 20 contadores. Muestre solo los resultados mayores a cero.
            contadores = contar_trabajo(arreglo_trabajos)
            for i in range(len(contadores)):
                if contadores[i] > 0:
                    print(f"La cantidad de trabajos de tipo {i} es: {contadores[i]}")

        if opcion == 4:
            # 4-      Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los
            # trabajos del arreglo
            promedio = round(calcular_promedio(arreglo_trabajos), 2)
            for i in range(len(arreglo_trabajos)):
                if arreglo_trabajos[i].importe > promedio:
                    print(f"El importe ${arreglo_trabajos[i].importe} es mayor al promedio (${promedio})")

        if opcion == 5:
            # 5-      Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t,
            # siendo num y t dos valores que se cargan por teclado. Si existe, mostrar sus datos. Si no existe, informar
            # con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo
            # el primero que encuentre.
            num = int(input("Ingrese numero de identificador a buscar: "))
            tipo_trabajo = int(input("ingrese tipo de trabajo como filtro: "))
            posicion = buscar_identificacion_tipo(arreglo_trabajos, num, tipo_trabajo)
            if posicion != -1:
                print("\nSe enconctro el trabajo buscado: ")
                print(arreglo_trabajos[posicion])
            else:
                print("\nNo se encontró ese trabajo, segui participando")

    print("\nGracias Por usar el servicio!")



if __name__ == '__main__':
    principal()


