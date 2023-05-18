"""Ingresar una secuencia de n números, de a uno por vez.
El valor de n se ingresa por teclado, validar que sea mayor a 0. Determinar:
a) Cuántos números ingresados terminan en 5
b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia
c) Cuántos números ingresados son mayores al anterior"""

primero = True
cont_fin5 = cont_primer_n = cont_mayor_ant =0

n = int(input("Ingrese un numero n (con cero corta): "))
while n != 0:
    if n % 5 == 0 and n % 2 == 1:
        cont_fin5 += 1

    if primero:
        primer_n = n
        cont_primer_n += 1
    elif n == primer_n:
        cont_primer_n += 1

    if not primero:
        if n > ant:
            cont_mayor_ant += 1
            #ant = n
    else:
        #ant = n
        primero = False

    ant =n
    n = int(input("Ingrese el siguiente numero n (con cero corta): "))

print ("\n", 25*"-", "Resultados", 25*"-")
print(f"Cantidad de numeros que terminan en 5: {cont_fin5}")
print(f"Cantidad de veces que aparece el primer numero ingresado ({primer_n}) en la secuencia: {cont_primer_n}")
print(f"Numeros ingresados que son mayores al anterior: {cont_mayor_ant}")

print(f"anterior: {ant}")


