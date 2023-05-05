
"""Una empresa debe calcular el total de comisiones que debe abonar por 
ventas realizadas por sus vendedores, para ello le solicita un sistemita
 que le permita calcular dicho montos.

Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores
(1 a 4). Usted debe solicitar el ingreso de la categoría del vendedor
y el total de la venta (el proceso termina cuando se ingrese una categoría
igual a cero) y acumular las comisiones de las ventas rendidas por los
vendedores de diferentes en base a los siguientes cálculos:

a) Categoría 1: cobra una comisión de 10%
b) Categoría 2: cobra una comisión de 25%
c) Categoría 3: cobra una comisión de 30%
d) Categoría 4: cobra una comisión de 40%
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar
por cada categoría de vendedores que tiene la empresa junto con el total general
"""
acumulador1 = 0
acumulador2 = 0
acumulador3 = 0
acumulador4 = 0
acumulador_general = 0
categoria = int(input("Ingrese la categoria del vendedor (1-4): "))

while 1 <= categoria <= 4:
    venta = int(input("Ingrese el monto de ventas: "))
    if categoria == 1:
        comision = 0.1 * venta
        acumulador1 += comision
        acumulador_general += comision
    elif categoria == 2:
        comision = 0.2 * venta
        acumulador2 += comision
        acumulador_general += comision
    elif categoria == 3:
        comision = 0.3 * venta
        acumulador3 += comision
        acumulador_general += comision
    elif categoria == 4:
        comision = 0.4 * venta
        acumulador4 += comision
        acumulador_general += comision

    categoria = int(input("Ingrese la categoria del siguiente vendedor (1-4): "))

print (f"Comisiones totales: ${acumulador_general}")
print (f"Comisiones categoria 1: $ {acumulador1}")
print (f"Comisiones categoria 2: $ {acumulador2}")
print (f"Comisiones categoria 3: $ {acumulador3}")
print (f"Comisiones categoria 4: $ {acumulador4}")