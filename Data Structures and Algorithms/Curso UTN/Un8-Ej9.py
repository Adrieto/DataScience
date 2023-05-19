import random

random.seed(37)

cant = 27000
lim_inf = -20000
lim_sup = 30000

acumulador_total = 0
acum_1 = 0
mayor = 0

cont_1 = cont_2 = cont_3 = cont_4 = cont_div7 = 0

for i in range (cant):
    n = random.randint(lim_inf, lim_sup)
    acumulador_total += 1
    if -20000 <= n < -5000:
        cont_1 += 1
    elif -5000 <= n < 15000:
        cont_2 += 1
    elif n >= 15000 and n % 9 == 0:
        cont_3 += 1

    if n >= 1000 and (n % 10 == 4 or n % 10 == 6):
        acum_1 += n
        cont_4 += 1

    if n > 0 and n % 2 == 1 and n % 10 != 1 and n > mayor:
        mayor = n

    if n % 7 == 0:
        cont_div7 += 1

porcentaje_div7 = cont_div7 * 100 // acumulador_total

print (f"entre -20000 y -4999: {cont_1}")
print (f"entre -5000 y 14999: {cont_2}")
print (f"mayores a 15000 y divisibles por 9: {cont_3}")
print(f"total acumulado: {acumulador_total}")
print(f"contador de lo de abajo: {cont_4}, {acum_1}")
print(f"Promedio de mayores a 1000 y que terminen en 4 o 6: {acum_1//cont_4}")
print(f"El mayor de los numeros positivos impares y que no terminan en 1: {mayor}")
print(f"Cantidad de divisibles por 7: {cont_div7}. Porcentaje sobre el total: {porcentaje_div7}%")