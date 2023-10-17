import soporte


# 0.)  Cree un arreglo c de 300000 casillas, inicializadas en cero.
# 1.)  Para cada número x del vector v de entrada:
#           1.1) Incremente en uno la casilla c[x]
# 2.)  Mostrar la cantidad de casilleros diferentes de cero que quedaron en el arreglo c.

def sort(vector):
    n = len(vector)
    for i in range(n-1):
        for j in range(i+1, n):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]


def valor_modal(contadores, vector):
    n = len(contadores)
    moda = -1
    maximo = 0
    for i in range(n):
        if contadores[i] > maximo:
            maximo = contadores[i]
            moda = i
        elif contadores[i] == maximo:
            moda = 0
    return moda, maximo


def principal():
    cant_datos = 300_000
    v = soporte.vector_known_range(cant_datos)
    contadores = cant_datos * [0]

    for nro in v:
        contadores[nro] += 1

    #indices_y_contadores = list(enumerate(contadores))
    #print(indices_y_contadores[0:20])

    moda, repeticiones = valor_modal(contadores, v)

    print(f"moda: {moda}. Se repitió {repeticiones}")
    print(contadores[0:20])
    #print(v[-100:-1])

    # cont_6 = 0
    # for i in range(cant_datos):
    #     if v[i] == 5:
    #         cont_6 += 1
    #         print(v[i])
    # print(f"contador_loco: {cont_6}")
    # print(contadores[0:10])





    # set_v = set(v)
    #
    # v_depurado_indexado = list(set_v)
    # print(len(v_depurado_indexado))
    # #moda, repeticiones = valor_modal(v_depurado_indexado, depurado)
    #
    # #print(f"Valor modal {moda} con {repeticiones} repeticiones")
    # #print(f"Vector original ordenado: {v}")

if __name__ == '__main__':
    principal()