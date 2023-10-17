# 3. Busqueda de primos
# Desarrollar un programa que permita generar un arreglo de n elementos. A partir de este arreglo, se pide lo siguiente:
#
# Generar un segundo arreglo con todos los números primos contenidos en el arreglo original.
# Determinar el promedio de los números del arreglo generado en el punto 1.

import vectores

def primos(vector):
    resultado = []
    largo = len(vector)
    primo = True
    for i in range(largo):
        for j in range(i):
            if vector[i] % vector[j] == 0 and vector[j] != 1 :
                primo = False
        if primo:
            resultado.append(vector[i])
        primo = True
    return resultado

def promedio_vector (vector):
    acum = 0
    n = len(vector)
    for numero in vector:
        acum += numero

    if n > 0:
        return acum/n
    else:
        return None




def main():
    n = 127
    vector_lista = [i for i in range(1, n)]
    vectores.mostrar_vector(vector_lista)

    # Generar un segundo arreglo con todos los números primos contenidos en el arreglo original.
    numeros_primos = primos(vector_lista)
    print(f"\nNumeros primos a partir del vector original: {numeros_primos}")

    # Determinar el promedio de los números del arreglo generado en el punto 1.
    print(f"Promedio de los elementos del vector: {promedio_vector(vector_lista)}")



if __name__ == '__main__':
    main()