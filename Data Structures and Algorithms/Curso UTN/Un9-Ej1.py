"""Desarrolle un programa que permita generar una sucesión de mil números enteros aleatorios,
 usando como semilla del generador al valor 11. Los números generados deben estar entre 1 y 2500
  (ambos incluidos). A partir de esa sucesión, el programa debe informar:

1) Cuántos números eran divisibles por 4 pero no por 8, y cuántos eran divisibles por ambos
2) El promedio de los valores mayores a 2000
3) Cuántos números eran menores al primer valor generado y qué porcentaje representan sobre el total de números
4) Si alguna vez aparecieron en la secuencia los valores extremos del intervalo (1, 2500)"""

import random
random.seed(11)

extremos = False
primero = True
cont_div4y8 = cont_div4 = cont_mayor_2000 = cont_menor_alprimero = 0
acum_mayor2000 = 0

for i in range (1000):
    n = random.randint(1,2500)

    if n%4 == 0 and n%8 == 0:
        cont_div4y8 += 1
    else:
        if n%4 == 0:
            cont_div4 += 1

    if n>2000:
        cont_mayor_2000 += 1
        acum_mayor2000 += n

    if n == 1 or n ==2500:
        extremos = True

    if primero:
        primer_valor = n
        primero = False
    else:
        if n < primer_valor:
            cont_menor_alprimero += 1

print(f"Los numeros solo divisibles por 4 son: {cont_div4}")
print(f"Los numeros divisibles por 4 y 8 son: {cont_div4y8}")
print(f"Valores mayores a 2000: {cont_mayor_2000}. Su promedio es {acum_mayor2000/cont_mayor_2000}")
print(f"\nCantidad de numeros menores al primer valor ({primer_valor}): {cont_menor_alprimero}")
print(f"Respecto al total de numeros, representan un {cont_menor_alprimero/1000 * 100}% \n")
print(f"Aparecieron los extremos (1 o 2500)?: {extremos}")
