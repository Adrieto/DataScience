# 2. Último y Primero
# Desarrollar un programa que permita cargar por teclado un vector de n elementos y luego:
#
# Informe cuántas veces se repite en el vector el último número ingresado
# Genere un nuevo vector, conteniendo sólo los elementos menores al primer valor ingresado.

from vectores import *


def repeticiones_ultimo_cargado(vector):
    ultimo = vector[-1]
    cont_ultimo = 0
    for elem in vector:
        if elem == ultimo:
            cont_ultimo += 1
    return cont_ultimo

def vector_menores_primero(vec):
    largo = len(vec)
    resultado = []
    for i in range(largo):
        if vec[i] < vec[0]:
            resultado.append(vec[i])
    return resultado



def main():
    n = int(input("Ingrese la cantidad de elementos del vector (mayor cero): "))
    vec = cargar_vector(n)
    mostrar_vector(vec)

    # Informe cuántas veces se repite en el vector el último número ingresado
    repeticiones_ultimo = repeticiones_ultimo_cargado(vec)
    print(f"\nLa cantidad de veces que se repite {vec[-1]} es: {repeticiones_ultimo}")

    # Genere un nuevo vector, conteniendo sólo los elementos menores al primer valor ingresado.
    resultados_primero = vector_menores_primero(vec)
    print(f"Vector con los elementos menores al primero ingresado: {resultados_primero}")




if __name__ == '__main__':
    main()