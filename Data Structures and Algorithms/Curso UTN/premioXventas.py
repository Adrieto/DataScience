"""Para calcular el premio de un vendedor, se ingresan 3 montos correspondientes a sus
ventas mensuales del último trimestre.
El premio es equivalente al 50% del menor monto vendido.
Si además todos los montos superan los $1000,
se agrega un 10% adicional al premio calculado.
Ejercicio tipo parcial """

m1 = int(input("ventas del primer mes: "))
m2 = int(input("ventas del segundo mes: "))
m3 = int(input("ventas del tercer mes: "))
premio = 0.5 * min (m1,m2,m3)

if m1>1000 and m2>1000 and m3>1000:
    premio += 0.5 * premio
print (f"el premio es: ${premio}")