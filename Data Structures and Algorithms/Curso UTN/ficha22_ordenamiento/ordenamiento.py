import random


def generate_random(v):
    # carga el arreglo con valores aleatorios...
    n = len(v)
    for i in range(n):
        v[i] = random.randint(1, 1000)


# comprueba si el arreglo está ordenado de menor a mayor...
def check(v):
    n = len(v)

    for i in range(n - 1):
        if v[i] > v[i+1]:
            return False

    return True


# ordenamiento por seleccion directa
def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


# ordenamiento por intercambio directo
def bubble_sort(v):
    n = len(v)
    for i in range(n-1):
        ordenado = True
        for j in range(n-i-1):
            if v[j] > v[j+1]:
                ordenado = False
                v[j], v[j+1] = v[j+1], v[j]
        if ordenado:
            break


# ordenamiento por inserción directa
def insertion_sort(v):
    n = len(v)
    for j in range(1, n):
        y = v[j]
        k = j - 1
        while k >= 0 and y < v[k]:
            v[k+1] = v[k]
            k -= 1
        v[k+1] = y


# ordenamiento de Shell
def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3


# Quicksort
def quick_sort(v):
    quick(v, 0, len(v) - 1)


def quick(v, izq, der):
    i, j = izq, der
    x = v[int((izq + der) / 2)]
    while i <= j:
        while v[i] < x and i < der:
            i += 1
        while x < v[j] and j > izq:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    if izq < j:
        quick(v, izq, j)
    if i < der:
        quick(v, i, der)


# Heapsort
def heap_sort(v):
    n = len(v)

    # Primera fase: crear el grupo inicial...
    for i in range(n):
        e = v[i]
        s = i
        f = (s - 1) // 2
        while s > 0 and v[f] < e:
            v[s] = v[f]
            s = f
            f = (s - 1) // 2
        v[s] = e

    # Segunda fase: se extrae la raiz, y se reordena el vector y el grupo...
    for i in range(n-1, 0, -1):
        valori = v[i]
        v[i] = v[0]
        f = 0
        if i == 1:
            s = -1
        else:
            s = 1
        if i > 2 and v[2] > v[1]:
            s = 2
        while s >= 0 and valori < v[s]:
            v[f] = v[s]
            f = s
            s = 2*f + 1
            if s + 1 <= i - 1 and v[s] < v[s+1]:
                s += 1
            if s > i - 1:
                s = -1
        v[f] = valori
