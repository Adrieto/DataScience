import random


def cargar_vector(n):
    vector = n * [0]
    for i in range(n):
        vector[i] = int(input(f"Ingrese el elemento {i} del vector"))
    return vector


def mostrar_vector(vector):
    for elem in vector:
        print(elem, end=",")


def vector_aleatorio(n, menor, mayor):
    """n: numero de elementos
    menor y mayor: valores maximos y minimos en el vector
    """
    vector_resultado = []
    for i in range(n):
        vector_resultado.append(random.randint(menor, mayor))
    return vector_resultado
