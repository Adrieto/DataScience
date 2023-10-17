# Mayores con el mismo índice
# Cargar por teclado dos vectores de tamaño n y, a partir de ellos, generar un tercer vector que contenga,
# para cada componente, el mayor valor entre las componentes homólogas (mismo índice) de los otros dos vectores.
#
# Por ejemplo, si se cargan los siguientes vectores a y b:
# a = [3, 4, 6]
# b = [8, 5, 1]         El resultado sería:  c = [8, 5, 6]


import vectores
from vectores import *

def comparacion(vector1, vector2):
    n = len (vector1)
    resultado = n * [0]
    for i in range(n):
        if vector1[i] > vector2[i]:
            resultado[i] = vector1[i]
        else:
            resultado[i] = vector2[i]
    return resultado





def main():
    cant_vectores = 2
    lista_vectores = [[], []] # Una lista de listas, me permite agregar valores
    n = int(input("Ingrese cantidad elementos de los dos vectores: "))

    for i in range(cant_vectores):
        print(f"-vector numero {i+1}-")
        lista_vectores[i] = vectores.cargar_vector(n)

    print(lista_vectores[0], lista_vectores[1])

    # Comparamos los vectores
    mayores_entre_homologos = comparacion(lista_vectores[0], lista_vectores[1])
    print(f"Los mayores homologos son: {mayores_entre_homologos}")



if __name__ == '__main__':
    main()




