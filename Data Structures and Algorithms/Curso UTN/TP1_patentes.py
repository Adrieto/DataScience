# TP1 Patentes y peajes
# Formatos posibles:

# Argentina: LLNNNLL     "AK348LZ"
# Bolivia:   LLNNNNN     "AP85986"
# Brasil:    LLLNLNN     "ASF5Q99"
# Paraguay:  LLLLNNN     "ASFQ849"
# Uruguay:   LLLNNNN     "ASF8492"
# Otro:      Cualquier otro formato

patente = input("Ingrese la patente del vehìculo: ")

# Chequeamos que el origen de las patentes:
if len(patente) == 7 and patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
    pais_procedencia = "Argentina"
elif len(patente) == 7 and patente[0:2].isalpha() and patente[2:7].isdigit():
    pais_procedencia = "Bolivia"
elif (
    len(patente) == 7
    and patente[0:3].isalpha()
    and patente[3].isdigit()
    and patente[4].isalpha()
    and patente[5:7].isdigit()
):
    pais_procedencia = "Brasil"
elif len(patente) == 7 and patente[0:4].isalpha() and patente[4:7].isdigit():
    pais_procedencia = "Paraguay"
elif len(patente) == 7 and patente[0:3].isalpha() and patente[3:7].isdigit():
    pais_procedencia = "Uruguay"
else:
    pais_procedencia = "Otro"

# tipo de vehiculo
print("Ingrese el tipo de vehiculo")
print('[0] - Motocicleta')
print('[1] - Automóvil')
print('[2] - Camión')
tipo_de_vehiculo = int(input("Ingrese el tipo de vehículo: "))

# Forma de pago
print("Ingrese la forma de pago: ")
print('[1] - Manual')
print('[2] - Telepeaje')
forma_de_pago = int(input("ingrese la forma de pago: "))

#Pais de la cabina
print("Ingrese el numero correspondiente al pais donde está la cabina")
print('[0] - Argentina')
print('[1] - Bolivia')
print('[2] - Brasil')
print('[3] - Paraguay')
print('[4] - Uruguay')
pais_de_la_cabina = int(input("La cabina esta en: "))

if pais_de_la_cabina == 0:
    cabina = "Argentina"
elif pais_de_la_cabina == 1:
    cabina = "Bolivia"
elif pais_de_la_cabina == 2:
    cabina = "Brasil"
elif pais_de_la_cabina == 3:
    cabina = "Paraguay"
elif pais_de_la_cabina == 4:
    cabina = "Uruguay"


# Distancia:
distancia = float(input("Ingrese los kilombretros recorridos desde la última cabina: "))

# Se establece el importe básico segun pais
if pais_de_la_cabina == 0 or pais_de_la_cabina == 3 or pais_de_la_cabina == 4:
    importe_basico = 300
elif pais_de_la_cabina == 2:
    importe_basico = 400
elif pais_de_la_cabina == 1:
    importe_basico = 200


# Ajuste de importe básico segun tipo de vehículo
if tipo_de_vehiculo == 0:
    importe_basico -= (0.5 * importe_basico)
elif tipo_de_vehiculo == 2:
    importe_basico += (0.6 * importe_basico)
else:
    importe_basico = importe_basico

# Importe final del ticket, segun forma de pago
if forma_de_pago == 2:
    valor_final_del_ticket = importe_basico - (0.1 * importe_basico)
else:
    valor_final_del_ticket = importe_basico


# Impresión del ticket:
print(f"\n\n  TICKET ESTACION DE PEAJE - {cabina}")
print(f"Pais de procedencia del vehículo: {pais_procedencia}")
print(f"Importe básico para el vehículo: ${importe_basico}")
print(f"Valor final del ticket: ${valor_final_del_ticket}")

if distancia > 0:
    promedio = valor_final_del_ticket/distancia
    print ("Valor promedio pagado por el vehículo por cada kilómetro recorrido: $", round(promedio,2))
else:
    print ("No aplica el cálculo de valor promedio por kilómetro")

