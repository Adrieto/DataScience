"""Desarrolle un programa completo en Python que permita generar una
sucesión de 20000 números enteros aleatorios, usando como semilla del
generador el numero 49 (es decir random.seed(49)). Los valores de
cada uno de esos 20000 números deben estar entre 1 y 45000 
(incluidos ambos) (DEBE usar random.randint(1, 45000) 
para generar esos números).
Suma de todos los números generados: 451459554
Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 
7 y cuántos eran múltiplos de 9.

Indicar el mayor entre todos aquellos números cuyo último dígito sea
mayor o igual a 5 pero menor o igual a 8.

Indicar cuantos números generados son pares menores a 15000.

Indicar el porcentaje entero que representa el punto anterior sobre el
total de números procesados. 
Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje
truncado, sin decimales. 
Aclaración 2: en el cálculo de este porcentaje, haga primero la
multiplicación que corresponda, y luego la división."""

import random

random.seed(49)
cant_aleatorios = 20000
lim_inf = 1
lim_sup = 45000

acumulador = 0
con_par_menor = con_mul9 = con_mul7 = con_mul5 = 0
mayor = 0

for i in range(cant_aleatorios):
    n = random.randint(lim_inf, lim_sup)
    acumulador += n

    if n % 9 == 0:
        con_mul9 += 1
    if n % 7 == 0:
        con_mul7 += 1
    if n % 5 == 0:
        con_mul5 += 1
    
    if n % 10 >= 5 and n % 10 <= 8 and n > mayor:
        mayor = n

    if n % 2 == 0 and n < 15000:
        con_par_menor += 1

porcentaje = (con_par_menor * 100 ) // cant_aleatorios

print (25*"-", "Resultados", 25*"-")
print(f"Verificacion: Acumulador da {acumulador} y debe ser 451459554")
print(f"multiplos de 5: {con_mul5}")
print(f"multiplos de 7: {con_mul7}")
print(f"multiplos de 9: {con_mul9}")
print(f"Mayor numero encontrado: {mayor}")
print(f"Cantidad de numeros pares <15000: {con_par_menor}")
print(f"Porcentaje sobre el total: {porcentaje}")

