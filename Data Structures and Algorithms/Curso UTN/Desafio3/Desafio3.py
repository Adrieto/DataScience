# 0.)  Cree los dos arreglos num y cont inicialmente vacíos (sin casilleros).
# 1.)  Para cada número x del arreglo de entrada:
#       1.1) Buscar x en el arreglo num y determinar el índice i de la casilla donde está almacenado.
#       1.2) ¿Existe x en el arreglo num (o sea: el valor de i es diferente de -1)?
#           Sí:  Sumar 1 al casillero cont[i].
#           No:  Agregar al final del arreglo num el número x, y agregar un 1 al final del arreglo cont.
# 2.)  Mostrar el tamaño final del arreglo num (para saber cuántos numeros diferentes aparecieron).

import soporte

def buscar(num, valor):
    n = len(num)
    contador_operaciones = 0
    for i in range(n):
        contador_operaciones += 1
        if num[i] == valor:
            return i, contador_operaciones
    return -1, contador_operaciones


def valor_modal(num, cont):
    n = len(num)
    moda = -1
    maximo = 0
    for i in range(n):
        if cont[i] > maximo:
            maximo = cont[i]
            moda = num[i]
        elif cont[i] == maximo:
            moda = 0
    return moda, maximo


def principal():
    cant_datos = 300_000
    v = soporte.vector_unknown_range(cant_datos)
    #print(f"Vector: {v}")
    num = []
    cont = []
    contador_total_operaciones = 0
    for i in range(len(v)):
        indice, contador_operaciones = buscar(num, v[i])
        contador_total_operaciones += contador_operaciones
        if indice != -1:
            cont[indice] += 1
        else:
            num.append(v[i])
            cont.append(1)
    #num =  [10,25, 3, 1, 8,30,11,95,23]
    #cont = [40,45,41,23,45,10,47,47,50]
    print(f"El numero total de operaciones para {cant_datos} datos es de {contador_total_operaciones}")

    moda, repeticiones = valor_modal(num, cont)

    print(f"El valor modal es {moda} y se repitió {repeticiones} veces" if moda != 0 else
          f"Hay mas de un valor modal! (devolvió {moda}, se repitió {repeticiones} veces")


if __name__ == '__main__':
    principal()

