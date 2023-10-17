# Desarrollar un programa controlado por menú de opciones para gestionar el catálogo de una zapatería.
# Por cada calzado se almacena código, talle y color. Se pide implementar las siguientes opciones:
#
#   1. Generar un vector con n datos aleatorios (para n que se ingresa por teclado)
#   2. Mostrar el contenido del vector generado
#   3. Almacenar el contenido del catálogo (ordenado por código) en el archivo catalogo.dat
#   4. Mostrar el contenido del archivo catalogo.dat
import random
import pickle
from zapatos import Zapato
import os.path


def menu():
    print("1) Generar un vector con n datos aleatorios")
    print("2) Mostrar el contenido del vector generado ")
    print("3) Almacenar el contenido del catálogo (ordenado por código) en el archivo catalogo.dat")
    print("4) Mostrar el contenido del archivo catalogo.dat")
    print("0) Salir")
    opcion = int(input("Elija una opcion: "))
    return opcion


def generacion_aleatoria(n, arreglo):
    COLORES = ("marron", "negro", "blanco", "azul", "gris")
    for i in range(n):
        codigo = random.randint(1, 50)
        talle = 2 * random.randint(12, 24)
        color = random.choice(COLORES)
        nuevo_zapato = Zapato(codigo, talle, color)
        arreglo.append(nuevo_zapato)


#   3. Almacenar el contenido del catálogo (ordenado por código) en el archivo catalogo.dat
def guardar_datos(zapatos, nombre_archivo):
    archivo = open(nombre_archivo, "wb")
    for zapato in zapatos:
        pickle.dump(zapato, archivo)
    archivo.close()

#   4. Mostrar el contenido del archivo catalogo.dat
def mostrar_datos_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        m = open(nombre_archivo, "rb")
        tamaño = os.path.getsize(nombre_archivo)
        cont_zapatos = 0
        while m.tell() < tamaño:
            nuevo_zapato = pickle.load(m)
            print(nuevo_zapato)
            cont_zapatos += 1
        print(f"\t\tArchivo cargado exitosamente, se leyeron {cont_zapatos} pares de zapatos")
    else:
        print(f'El archivo "{nombre_archivo}" no existe.')


def principal():
    opcion = -1
    n = 100
    zapatos = []
    nombre_archivo = "catalogo.dat"

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            generacion_aleatoria(n, zapatos)
        elif opcion == 4:
            mostrar_datos_archivo(nombre_archivo)
        elif len(zapatos) == 0:
            print("\t\tPrimero debe cargarse el vector\n")
        elif opcion == 2:
            for zapato in zapatos:
                print(zapato)
        elif opcion == 3:
            guardar_datos(zapatos, nombre_archivo)


    print("CHAU")

if __name__ == '__main__':
    principal()