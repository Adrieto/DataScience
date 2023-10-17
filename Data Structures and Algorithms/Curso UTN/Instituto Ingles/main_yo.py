# 5. (Parcial 2020) La Academia de Ingles
# Una academia de inglés para niños de escolaridad primaria y nivel inicial, desea un programa para
# procesar los datos de sus alumnos. Por cada alumno se tienen los siguientes datos: DNI del alumno, el nombre
# del alumno, el apellido del alumno, DNI del Tutor (adulto responsable del niño), el importe de la cuota y
# el nivel en el que cursa el niño (un valor entre 0 y 12 incluidos, de la forma 0: Inicial, 1: Primer Junior,
# 2: Primer Younger, etc.). Se desea almacenar la información referida a los n alumnos en un arreglo de objetos
# de clase Alumno (definir la clase Alumno y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de los n alumnos. Valide que el número de nivel sea un valor entre 0 y 12
# (ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática
# (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
#
# 2- Mostrar todos los datos de todos los alumnos, en un listado ordenado de menor a mayor según el apellido del alumno.
#
# 3- Usando el arreglo creado en el punto 1, determine la cantidad de alumnos que cursan en cada nivel
# (o sea, 13 contadores). Muestre sólo los resultados diferentes de 0.
#
# 4- Determinar el monto total que debe abonar el Tutor con número de DNI igual a x, siendo x un valor que se
# carga por teclado (sumar los importes de las cuotas de los niños que el Tutor tiene a su cargo).
#
# 5- Determinar si existe un alumno con un apellido que sea igual a x (siendo x un valor que se carga por teclado).
# Si existe, modificar el importe de su cuota con un descuento del 10 % y mostrar los datos actualizados del alumno.
# Si no existe, informar con un mensaje. Si existe más de un objeto que coincida con esos parámetros de búsqueda,
# debe mostrar sólo el primero que encuentre.

import random
from alumno_yo import *


def menu():
    print("Menu de opciones:")
    print("1) Cargar el arreglo pedido con los datos de los n alumnos")
    print(
        "2) Mostrar todos los datos de todos los alumnos, en un listado ordenado de menor a mayor según el apellido del alumno")
    print("3) Usando el arreglo creado en el punto 1, determine la cantidad de alumnos que cursan en cada nivel")
    print("4) Determinar el monto total que debe abonar el Tutor con número de DNI igual a x.")
    print("5) Determinar si existe un alumno con un apellido que sea igual a x ")
    print("0) Salir")
    opcion = int(input("\nElija una opcion:"))
    return opcion


def validar_entre(limite_inf, limite_sup, mensaje):
    numero = limite_inf - 1
    while numero < limite_inf or numero > limite_sup:
        numero = int(input(mensaje))
        if numero < limite_inf or numero > limite_sup:
            print(f"ERROR! El numero debe estar entre {limite_inf} y {limite_sup}")
    return numero


def validar_mayor_que(limite, mensaje):
    numero = limite - 1
    while numero <= limite:
        numero = int(input(mensaje))
        if numero <= limite:
            print(f"ERROR! El numero debe ser mayor a {limite}")
    return numero


def cargar_arreglo(n):
    nombres = ["Adrian", "Lucas", "Camila", "Rocío", "Pablo", "Juanjo"]
    apellidos = ["Parodi", "Balcarce", "Messi", "Ronaldo", "Marley", "Alvarez"]
    arreglo_alumnos = []
    for i in range(n):
        dni_alumno = random.randint(40000000, 70000000)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        dni_tutor = random.randint(32000000, 32000010)
        #dni_tutor = 32608635
        importe = round(random.uniform(150, 1200), 2)
        nivel = validar_entre(1, 12, "Introduzca un numero entre 1 y 12: ")

        nuevo_alumno = Alumno(dni_alumno, nombre, apellido, dni_tutor, importe, nivel)
        arreglo_alumnos.append(nuevo_alumno)
    return arreglo_alumnos


def cargar_aleatoria(n):
    nombres = ["Adrian", "Lucas", "Camila", "Rocío", "Pablo", "Juanjo"]
    apellidos = ["Parodi", "Balcarce", "Messi", "Ronaldo", "Marley", "Alvarez"]
    arreglo_alumnos = []
    for i in range(n):
        dni_alumno = random.randint(40000000, 70000000)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        dni_tutor = random.randint(32000000, 32000010)
        importe = round(random.uniform(150, 1200), 2)
        nivel = random.randint(1,12)

        nuevo_alumno = Alumno(dni_alumno, nombre, apellido, dni_tutor, importe, nivel)
        arreglo_alumnos.append(nuevo_alumno)
    return arreglo_alumnos


def ordenar(arreglo_alumnos):
    n= len(arreglo_alumnos)
    for i in range(n-1):
        for j in range(i, n):
            if arreglo_alumnos[i].apellido > arreglo_alumnos[j].apellido:
                arreglo_alumnos[i], arreglo_alumnos[j] = arreglo_alumnos[j], arreglo_alumnos[i]
            elif arreglo_alumnos[i].apellido == arreglo_alumnos[j].apellido:
                if arreglo_alumnos[i].nombre > arreglo_alumnos[j].nombre:
                    arreglo_alumnos[i], arreglo_alumnos[j] = arreglo_alumnos[j], arreglo_alumnos[i]


def cantidad_alumnos_nivel(arreglo_alumnos):
    n = len(arreglo_alumnos)
    contadores = 12 * [0]
    for i in range(n):
        numero = arreglo_alumnos[i].nivel
        contadores[numero-1] += 1
    return contadores

# 4- Determinar el monto total que debe abonar el Tutor con número de DNI igual a x
def monto_tutor(arreglo_alumnos, dni_tutor):
    n = len (arreglo_alumnos)
    monto_total = 0
    for i in range(n):
        if dni_tutor == arreglo_alumnos[i].dni_tutor:
            monto_total += arreglo_alumnos[i].cuota
    return monto_total


# 5- Determinar si existe un alumno con un apellido que sea igual a x (siendo x un valor que se carga por teclado).
# Si existe, modificar el importe de su cuota con un descuento del 10 % y mostrar los datos actualizados del alumno.
# Si no existe, informar con un mensaje. Si existe más de un objeto que coincida con esos parámetros de búsqueda,
# debe mostrar sólo el primero que encuentre.
def encontrar(arreglo_alumnos, x):
    existe = False
    for alumno in arreglo_alumnos:
        if alumno.apellido == x:
            existe = True
            alumno.cuota *= 0.9
            return alumno


def main():
    opcion = -1
    while opcion != 0:
        opcion = menu()

        # 1) Cargar el arreglo pedido con los datos de los n alumnos"
        if opcion == 1:
            n = validar_mayor_que(0, "Ingrese cantidad de registros a generar: ")
            arreglo_alumnos = cargar_aleatoria(n)

        # 2- Mostrar todos los datos de todos los alumnos ordenados de menor a mayor según el apellido del alumno
        if len(arreglo_alumnos) > 0:
            if opcion == 2:
                ordenar(arreglo_alumnos)
                for i in range(n):
                    print(arreglo_alumnos[i])

        # 3- Usando el arreglo creado en el punto 1, determine la cantidad de alumnos que cursan en cada nivel
            elif opcion == 3:
                contadores = cantidad_alumnos_nivel(arreglo_alumnos)
                for i in range(len(contadores)):
                    if contadores[i]>0:
                        print(f"contadores nivel {i+1}: {contadores[i]}")

        # 4- Determinar el monto total que debe abonar el Tutor con número de DNI igual a x
            elif opcion == 4:
                dni_buscado = 32608635
                monto_total = monto_tutor(arreglo_alumnos, dni_buscado)
                print(f"El monto total a pagar por el tutor con DNI: {dni_buscado} es: {monto_total}")

            # 5- Determinar si existe un alumno con un apellido que sea igual a x (siendo x un valor que se carga por teclado).
            # Si existe, modificar el importe de su cuota con un descuento del 10 % y mostrar los datos actualizados del alumno.
            # Si no existe, informar con un mensaje. Si existe más de un objeto que coincida con esos parámetros de búsqueda,
            # debe mostrar sólo el primero que encuentre.
            elif opcion == 5:
                x = input("Ingrese el apellido a buscar: ")
                encontrado = encontrar(arreglo_alumnos, x)
                if encontrado:
                    print(f"Alumno encontrado:\n {encontrado}")
                else:
                    print(f"No se encontró el alumno {x}")
        else:
            print("Todavia no se cargaron datos. Carguelos con la opcion 1")




    print("Proceso finalizado. Gracias")


if __name__ == '__main__':
    main()
