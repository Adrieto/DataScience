"""Crear un programa que permita calcular los impuestos que debe pagar un auto,
conociendo su modelo (año de fabricación) y tipo (P: Particular/T: Taxi/R: Remis).
Para calcular los impuestos, tener en cuenta que:
a. Los autos particulares de menos de 10 años de antigüedad pagan $200,
entre 10 y 20 años pagan $150 y no pagan impuestos los que tienen más de 20 años.
b. Los taxis pagan impuestos como auto particular, más $150 por la licencia de taxi.
c. Los remises pagan $100 por cada año de antigüedad de su vehículo."""

tipo = input ("ingrese el tipo de auto (P: Particular/T: Taxi/R: Remis): ")
modelo = int(input ("ingrese año de fabricacion: "))

# Año actual
actual = 2023
antiguedad = actual - modelo

if tipo != "R" or tipo != "r":
    output= "particular"  
    if antiguedad < 10:
        impuesto = 200
    elif 10 <= antiguedad <= 20:
        impuesto = 150
    else:
        impuesto = 0

    # Si el vehículo es un taxi:    
    if tipo == "t" or tipo == "T":
        impuesto += 150
        output = "taxi"

else:
    output = "remis"
    impuesto = 100 * antiguedad

print (f"El impuesto que debe pagar por su vehiculo tipo {output} de {antiguedad} años de antigüedad \n"
       f"es de ${impuesto}")