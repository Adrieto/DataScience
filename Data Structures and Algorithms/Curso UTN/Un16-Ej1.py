# 1. Ordenar y buscar
# Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100 inclusive (pueden existir duplicados).
# A partir de ese arreglo:
#
# Ordenarlo de forma ascendente y mostrarlo
# Buscar un elemento x dentro del arreglo (x se ingresa por teclado). Si no existe, informarlo. Si existe,
# determinar cuántos valores impares mayores a x se encontraron en el arreglo.

import vectores
from modulos.sort_find import *

def impares_mayores_a_valor(vector, valor):
    cont_impares_mayores_a_valor = 0
    for i in range(len(vector)):
        if vector[i] > valor and vector[i] % 2 == 1:
            cont_impares_mayores_a_valor += 1
    return cont_impares_mayores_a_valor


def main():

    n = 20
    menor = 1
    mayor = 100
    vector_aleatorios = vectores.vector_aleatorio(n, menor, mayor)

    print(f"Desordenado: {vector_aleatorios}")
    # Ordeno de forma ascendente y muestro el vector:
    ordenar(vector_aleatorios, descendente=False)
    print(f"Ordenado: {vector_aleatorios}")

    # Buscar un elemento x dentro del arreglo (x se ingresa por teclado). Si no existe, informarlo. Si existe,
    # determinar cuántos valores impares mayores a x se encontraron en el arreglo.
    buscado = 10
    posicion_buscado = binary_search(vector_aleatorios, buscado)
    print("Posicion del valor buscado en el arreglo:", end=" ")
    print(posicion_buscado if posicion_buscado >= 0 else "no se encontró")
    print(f"Valor buscado: {buscado}, Valor encontrado: "
          f"{vector_aleatorios[posicion_buscado] if posicion_buscado != -1 else 'No se encontró'} ")

    impares_mayores_a_buscado = impares_mayores_a_valor(vector_aleatorios, buscado)

    print(f"La cantidad de impares mayores al valor {buscado} es: {impares_mayores_a_buscado}")



if __name__ == '__main__':
    main()