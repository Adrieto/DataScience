"""Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero.
Determinar:
a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
b) Determinar la cantidad de números que son el cuadrado del número anterior
c) Determinar la posición del mayor elemento impar de la secuencia"""

import math
cont_total = cont_div3 = cont_cuadrado_del_anterior = mayor = posicion = 0
primero = True

n = int (input("ingrese un numero n: "))

while n!=0:
    cont_total += 1
    if n % 3 == 0:
        cont_div3 += 1
    if cont_total > 1 and n == math.pow(ant,2):
        cont_cuadrado_del_anterior += 1
    if n % 2 != 0:
        if primero:
            mayor = n
            posicion = cont_total
            primero = False
        else:
            if n > mayor:
                mayor = n
                posicion = cont_total
    ant = n
    n = int(input("ingrese un numero n: "))

porcentaje_3 = cont_div3 / cont_total * 100
print (f"Cantidad de numeros divisibles por 3: {cont_div3}. Representan un {round(porcentaje_3,2)}% del total")
print (f"Cantidad de numeros que son el cuadrado del anterior: {cont_cuadrado_del_anterior}")
print (f"Posicion del mayor elemento impar de la secuencia: {posicion}. Es el numero: {mayor}")
