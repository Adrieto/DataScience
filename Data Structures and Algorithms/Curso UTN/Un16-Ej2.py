# Ingresar (o generar de manera aleatoria) los legajos de los n alumnos de un curso, siendo n un valor
# que se carga por teclado, y almacenarlos en un arreglo unidimensional. Se pide para ello:
#
# a - Ordenar el arreglo de menor a mayor. Mostrar por pantalla como quedó.
#
# b - Buscar en el arreglo el alumno con el legajo x, x se ingresa por teclado. Si existe mostrarlo,
# si no mostrar un mensaje de error.

import random

def crear_arreglo(n):
    vector = n * ["0"]
    for i in range(n):
        while not vector[i].isdigit() or int(vector[i]) <= 0:
            vector[i] = input(f"ingrese elemento {i} del vector: ")

    return vector

def crear_arreglo_aleatorio(n):
    vector = n * [0]
    for i in range(n):
        vector[i] = random.randint(100, 999)
    return vector

def ordenar(vector):
    n = len(vector)
    for i in range(n-1):
        for j in range(i+1, n):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]

def mostrar_vector(vector):
    for i in range(len(vector)):
        print(f"Elemento {i} del vector: {vector[i]}")

def buscar(x, vector):
    n = len(vector)
    izq = 0
    der = n-1

    while izq <= der:
        posicion_busqueda = (izq + der) // 2
        if vector[posicion_busqueda] == x:
            return posicion_busqueda
        elif vector[posicion_busqueda] < x:
            izq = posicion_busqueda + 1
        elif vector[posicion_busqueda] > x:
            der = posicion_busqueda - 1
    return -1



def main():
    n = int(input("ingresar cantidad de alumnos: "))
    lista_alumnos = crear_arreglo_aleatorio(n)
    print(f"Lista desordenada: {lista_alumnos}")
    #mostrar_vector(lista_alumnos)
    ordenar(lista_alumnos)
    print(f"Lista Ordenada: {lista_alumnos}")
    alumnoX = int(input("Ingrese el legajo del alumno a buscar: "))

    posicion_alumno = buscar(alumnoX, lista_alumnos)
    if posicion_alumno != -1:
        print (f"El alumno de legajo {alumnoX}, se encontró en la posicion {posicion_alumno}")
    else:
        print("NO se encontró al alumno")




if __name__ == '__main__':
    main()