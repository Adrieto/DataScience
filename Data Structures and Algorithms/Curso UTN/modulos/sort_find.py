def ordenar(vector, descendente=False):
    n = len(vector)
    for i in range(n - 1):
        for j in range(i + 1, n):

            if vector[j] < vector[i] and descendente == False:
                vector[j], vector[i] = vector[i], vector[j]

            elif vector[j] > vector[i] and descendente == True:
                vector[j], vector[i] = vector[i], vector[j]


def binary_search(vector, valor_buscado):
    n = len(vector)
    izq = 0
    der = n - 1

    while izq <= der:
        medio = (izq + der) // 2
        if vector[medio] == valor_buscado:
            posicion_valor_buscado = medio
            return posicion_valor_buscado

        elif vector[medio] > valor_buscado:
            der = medio - 1
        elif vector[medio] < valor_buscado:
            izq = medio + 1

    return -1


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1     # Esto ajusta el valor de h inicial...
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3
