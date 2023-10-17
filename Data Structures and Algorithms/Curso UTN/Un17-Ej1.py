# 1. Estudio climatológico
# Como parte de un estudio climatológico, se desea un programa que permita obtener una serie de estadísticas
# a partir de un conjunto de muestras de temperatura.
#
# Se pide un programa que:
#
# Ingrese n muestras de temperatura, donde cada muestra contiene la temperatura registrada,
# la región donde se registró la misma (1-20), y el día del mes en el que se registró la temperatura
# Determinar el promedio general de temperatura

# Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor
# Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado.
# Determinar la cantidad de muestras por region (20 contadores)

import random

def cargar_datos (temperatura, region, dia_mes):
    n = len (temperatura)
    for i in range(n):
        temperatura[i] = int(input(f"Cargue el dato de temperatura {i}: "))
        region[i] = int(input(f"Cargue el dato de region {i} - Entre 1 y 20: "))
        dia_mes[i] = int(input(f"Cargue el dato del dia del mes {i}: "))

def cargar_datos_aleatorios (temperatura, region, dia_mes):
    n = len(temperatura)
    for i in range(n):
        temperatura[i] = random.randint(0,9)
        region[i] = random.randint(1,8)
        dia_mes[i] = random.randint(1,9)


def ordenar (temperatura, region, dia_mes, region_deseada):
    # Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor
    n = len(temperatura)
    temperatura_filtrada = []
    region_filtrada = []
    dia_mes_filtrada = []

    for i in range(n):
        if region[i] == region_deseada:
            temperatura_filtrada.append(temperatura[i])
            dia_mes_filtrada.append(dia_mes[i])

    m = len(dia_mes_filtrada)
    for i in range(m-1):
        for j in range(i+1, m):
            if dia_mes_filtrada[i] > dia_mes_filtrada[j]:
                dia_mes_filtrada[i], dia_mes_filtrada[j] = dia_mes_filtrada[j], dia_mes_filtrada[i]
                temperatura_filtrada[i], temperatura_filtrada[j] = temperatura_filtrada[j], temperatura_filtrada[i]


    return dia_mes_filtrada, temperatura_filtrada

# Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado.
def temperatura_mayor_a_valor_en_region(vector_temp, vector_region, valor_region, valor_temp):
    for i in range(len(vector_region)):
        if vector_region[i] == valor_region:
            if vector_temp[i] > valor_temp:
                return i
    return -1



def promedio(vector):

    n = len(vector)
    sumador = 0
    for i in range(n):
        sumador += vector[i]
    return sumador / n

def cantidad_muestras_por_region (region, cantidad_contadores):
    contadores = cantidad_contadores * [0]
    n = len(region)
    for i in range(n):
        numero = region[i]
        contadores[numero-1] += 1
    return contadores


def main():
    n = int(input("Ingrese cantidad de datos en los arreglos: "))
    temperatura = n * [0]
    region = n * [0]
    dia_mes = n * [0]
    cargar_datos_aleatorios(temperatura, region, dia_mes)
    print(f"temperaturas: {temperatura}")
    print(f"region: {region}")
    print(f"dia_mes: {dia_mes}")
    #print (f"El promedio de temperaturas es: {promedio(temperatura)}")

    # Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado.
    region_deseada = 1
    filtrado_dia_mes, filtrado_temperatura = ordenar(temperatura, region, dia_mes, region_deseada)
    print(f"Orden segun la region {region_deseada}:")
    print(f"Temperaturas: {filtrado_temperatura}")
    print(f"Dia: {filtrado_dia_mes} \n")

    # Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado.
    valor_region = 2
    valor_temp = 8
    posicion = temperatura_mayor_a_valor_en_region(temperatura, region, valor_region, valor_temp)
    print(f"Se encontró una T mayor en la posicion: {posicion} " if posicion != -1 else f"No se encontró")

    # Determinar la cantidad de muestras por region (20 contadores)
    cantidad_contadores = 8
    contadores = cantidad_muestras_por_region(region, cantidad_contadores)
    print(f"Contadores por region: {contadores}")



if __name__ == '__main__':
    main()