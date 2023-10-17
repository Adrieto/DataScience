# 2. Estadística con dados
# # Para realizar una prueba estadística, se lanzan simultáneamente 2 dados y se anotan los resultados obtenidos.
# # Al cabo de n lanzamientos, se necesita determinar:
# #
# # Cuántas veces se obtuvo el mismo valor en ambos dados y qué porcentaje representa sobre el total de lanzamientos.
# # En qué lanzamiento se dio por primera vez una suma impar entre ambos dados
# # Cuál fue el mayor valor que apareció en cada dado y cuántas veces se presentó
# # Cuántas veces apareció cada una de las sumas posibles entre ambos dados. Es decir: cuántas veces sumaron 2, cuántas
# # veces sumaron 3, y así sucesivamente
# # Determinar la cantidad de tiradas en las que la suma de ambos dados fue mayor que la suma promedio de todas las tiradas
# # Desarrollar un programa que permita simular esta situación, guardando en vectores paralelos los valores de ambos dados.

import random

def lanzar_dados(n):
    lanzamientos1 = []
    lanzamientos2 = []
    for i in range(n):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        lanzamientos1.append(dado1)
        lanzamientos2.append(dado2)
    return lanzamientos1, lanzamientos2


def mismo_valor (lanzamientos1, lanzamientos2):
    n = len(lanzamientos1)
    cont_mismo_valor = 0
    for i in range(n):
        if lanzamientos1[i] == lanzamientos2[i]:
            cont_mismo_valor += 1
    return cont_mismo_valor

# En qué lanzamiento se dio por primera vez una suma impar entre ambos dados
def suma_es_impar(lanzamientos1, lanzamientos2):
    posicion = 0
    for i in range(len(lanzamientos1)):
        if (lanzamientos1[i] + lanzamientos2[i]) % 2 == 1:
            posicion = i
            return posicion


def mayor_valor(lanzamientos1, lanzamientos2):
    mayor_valor_dado1 = mayor_valor_dado2 = cont_mayor_valor1 = cont_mayor_valor2 = 0
    # Dado 1
    for i in range(len(lanzamientos1)):
        if lanzamientos1[i] > mayor_valor_dado1:
            mayor_valor_dado1 = lanzamientos1[i]
            cont_mayor_valor1 = 1

        elif lanzamientos1[i] == mayor_valor_dado1:
            cont_mayor_valor1 += 1

        # Dado 2
        if lanzamientos2[i] > mayor_valor_dado2:
            mayor_valor_dado2 = lanzamientos2[i]
            cont_mayor_valor2 = 1

        elif lanzamientos2[i] == mayor_valor_dado2:
            cont_mayor_valor2 += 1
    return (mayor_valor_dado1, mayor_valor_dado1), (cont_mayor_valor1, cont_mayor_valor2)

# Cuántas veces apareció cada una de las sumas posibles entre ambos dados.
def sumas_posibles(lanzamiento1, lanzamiento2):
    n = 11
    contadores = n * [0]
    for i in range(len(lanzamiento1)):
        suma = lanzamiento1[i] + lanzamiento2[i]
        contadores[suma-2] += 1
    return contadores

# Determinar la cantidad de tiradas en las que la suma de ambos dados fue mayor que la suma promedio de todas las tiradas
def promedio_sumas(lanzamientos1, lanzamientos2):
    n = len(lanzamientos1)
    sumador = 0
    for i in range (n):
        sumador += (lanzamientos1[i] + lanzamientos2[i])
    return sumador / n

def cant_mayores_promedio(lanzamientos1, lanzamientos2):
    n = len(lanzamientos1)
    contador = 0
    promedio = promedio_sumas(lanzamientos1, lanzamientos2)
    for i in range(n):
        if promedio < (lanzamientos1[i] + lanzamientos2[i]):
            contador += 1

    return contador



def main():
    n = 100

    lanzamientos1, lanzamientos2 = lanzar_dados(n)

    # Cuántas veces se obtuvo el mismo valor en ambos dados y qué porcentaje representa sobre el total de lanzamientos.
    cont_mismo_valor = mismo_valor(lanzamientos1, lanzamientos2)
    # Porcentaje
    porcentaje = (cont_mismo_valor * 100) / n

    print(f"porcentaje de veces que se obtuvo el mismo valor en ambos dados: {porcentaje}")

    # Cuál fue el mayor valor que apareció en cada dado y cuántas veces se presentó?
    valores, apariciones = mayor_valor(lanzamientos1, lanzamientos2)

    for i in range(len(valores)):
        print (f"El mayor valor obtenido en el dado {i+1} es: {valores[i]} y apareció {apariciones[i]} veces")

    # En qué lanzamiento se dio por primera vez una suma impar entre ambos dados
    posicion = suma_es_impar(lanzamientos1, lanzamientos2)
    print(f"El indice de la primera suma impar es: {posicion}")

    # Cuántas veces apareció cada una de las sumas posibles entre ambos dados.
    contador_sumas = sumas_posibles(lanzamientos1, lanzamientos2)
    print(f"Suma de contadores (de 2 a 12): {contador_sumas}")

    # Determinar la cantidad de tiradas en las que la suma de ambos dados fue mayor que la suma promedio de todas las tiradas
    cantidad_mayores_promedio = cant_mayores_promedio(lanzamientos1, lanzamientos2)
    promedio = promedio_sumas(lanzamientos1, lanzamientos2)
    print(f"Cantidad de veces que se superó el promedio {promedio} es de: {cantidad_mayores_promedio}")

    print("\n", lanzamientos1)
    print(lanzamientos2)


if __name__ == '__main__':
    main()