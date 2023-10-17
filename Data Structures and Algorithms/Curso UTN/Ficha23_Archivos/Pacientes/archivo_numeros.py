import io
import os.path
import pickle
import random


def generar_archivo(n):
    archivo = open("numeros.dat", "ab")
    for i in range(n):
        nro = random.randint(1, 1000000)
        pickle.dump(nro, archivo)
    archivo.close()


def contar_mayores_promedio():
    nombre_archivo = "numeros.dat"
    archivo = open(nombre_archivo, "rb")

    size = os.path.getsize(nombre_archivo)
    suma = cant = 0
    while archivo.tell() < size:
        nro = pickle.load(archivo)
        suma += nro
        cant += 1

    promedio = suma/cant
    print("El promedio es:", promedio)
    mayores = 0
    archivo.seek(-1000, io.SEEK_END)
    print(archivo.tell())
    while archivo.tell() < size:
        nro = pickle.load(archivo)
        if nro > promedio:
            mayores += 1

    print("Hay", mayores, "números mayores al promedio")

    archivo.close()


def principal():
    # n = int(input("Ingrese cantidad de números: "))
    # n = 100000
    # generar_archivo(n)

    numeros = contar_mayores_promedio()


if __name__ == '__main__':
    principal()