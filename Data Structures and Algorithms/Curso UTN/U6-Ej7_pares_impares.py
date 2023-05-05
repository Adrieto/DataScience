"""Se pide desarrollar un programa que permita leer una serie de números.
La finalización de carga de datos se presenta cuando el usuario ingrese
un número negativo.
Los requerimientos funcionales del programa son:
a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
b) Cantidad de valores pares ingresados.
c) Cantidad de valores impares ingresados.
d) Informar si en la carga de números se ingreso al menos un número 0.
e) Informar si la serie contiene solo números pares e impares alternados
Para este, se debe guardar el numero anterior, para poder comparar
"""

n = int (input("ingresa un numero entero: "))
c_p = 0
c_imp = 0
suma = 0
paso_cero = False
se_alterno = True
primero = True

while n >= 0:
    if n%2 == 0:
        c_p += 1
    else:
        c_imp += 1

    if 50 <= n <= 100:
        suma += n

    if n == 0:
        paso_cero = True

    if not primero and ant%2 == n%2:
        se_alterno = False
    
    primero = False
    ant = n
    n = int (input("ingresa un numero entero: "))

print(f"sumatoria numeros entre 50 y 100: {suma}")
print(f"Cantidad de valores pares: {c_p}")
print(f"Cantidad de valores impares: {c_imp}")
print(f"Ingresó algun cero? {paso_cero}")
print(f"Solo pares o impares alternados? {se_alterno}")