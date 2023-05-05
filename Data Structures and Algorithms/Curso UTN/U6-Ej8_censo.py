"""Censo Unidad 6 Ejercicio 8
Desarrollar un programa que permita procesar los datos del último censo de una
pequeña población. Por cada habitante se ingresa: sexo (M/F) y edad. 
La carga de datos finaliza al ingresar cualquier otro valor para sexo.

El programa debe informar:
a) A qué sexo corresponde la mayor cantidad de habitantes 
(considerar que puede ser igual)
b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
c) Si hay algún varón que supere los 80 años de edad"""


cant_hom = 0
cant_muj = 0
cant_muj_escolar = 0
hom_mayor80 = False

sexo = input("Ingrese sexo (M/F): ").upper()
while sexo == "M" or sexo == "F" :
    edad = int(input("ingrese edad: "))   
    if sexo == "M":
        cant_hom += 1
        if edad > 80:
            hom_mayor80 = True
    elif sexo == "F":
        cant_muj += 1
        if 4 <= edad <= 18:
            cant_muj_escolar += 1
    
    sexo = input("Ingrese sexo (M/F): ").upper()

print (f"cantidad de hombres: {cant_hom}")
if hom_mayor80:
    print("Hay hombres mayores de 80 años en este censo")
else: 
    print("NO hay hombres de mas de 80 años")

print (f"cantidad de mujeres: {cant_muj}")
print (f"cantidad de en edad escolar: {cant_muj_escolar}")
    

