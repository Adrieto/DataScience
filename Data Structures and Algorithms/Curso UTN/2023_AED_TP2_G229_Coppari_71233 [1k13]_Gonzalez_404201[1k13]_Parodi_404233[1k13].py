# TP1 Patentes y peajes
# Formatos posibles:

# Argentina: LLNNNLL     "AK348LZ"
# Bolivia:   LLNNNNN     "AP85986"
# Brasil:    LLLNLNN     "ASF5Q99"
# Paraguay:  LLLLNNN     "ASFQ849"
# Uruguay:   LLLNNNN     "ASF8492"
# Chile:      LLLLNN
# Otro:      Cualquier otro formato

# VER SI EL ARCHIVO DEBE ABRIRSE INTRODUCIENDO EL NOMBRE POR TECLADO!!!!
#archivo = open(input("Ingrese el nombre de archivo de texto: "))
archivo = open("peaje25.txt")
lines = archivo.readlines()
archivo.close()

#for line in lines:
#    print(line, end="")

## OTRA FORMA
archivo = open("peaje3.txt")
texto = archivo.read()
archivo.close()
empty_string = "\n"
#print(f"Largo texto: {len(texto)}, ultima letra: {texto[-1]}, es vacia?: {texto[-1] == empty_string}")

cont_letra = 0
cont_linea = 0
linea = ""

# Para saltear la primera linea
cont_inicio = 0
idioma_codigo = ("PT", "ES")

while texto[cont_inicio] != "\n":
    cont_inicio += 1
    print (texto[cont_inicio], end="")

# Verificiacion de idioma
if "PT" in texto[0:cont_inicio]:
    idioma = "Portugués"
elif "ES" in texto[0:cont_inicio]:
    idioma = "Español"

# Procesamiento linea a linea de patentes:
texto_patentes = texto[cont_inicio:-1]

for char in (texto_patentes):
    linea += str(char)
    cont_letra += 1
    if cont_letra % 14 == 0:
        cont_linea += 1
        print(linea)

        # Se asignan los datos necesarios a partir de la linea:
        patente = linea[1:8]
        tipo_vehiculo = linea[8]
        forma_pago = linea[9]
        pais_procedencia = linea[10]
        kms = linea [11:14]
        print(f"{patente} + {tipo_vehiculo} + {forma_pago} + {pais_procedencia} + {kms}")
        #print(f"{patente[1] == empty_string}")

        # Se reinician contadores
        cont_letra = 0
        linea = ""








"""patente = input("Ingrese la patente del vehículo: ")

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
elif len(patente) == 7 and patente[0] == " " and patente[1:5].isalpha() and patente[5:7].isdigit():
    pais_procedencia = "Chile"
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

# Se establece el importe BASE segun pais
if pais_de_la_cabina == 0 or pais_de_la_cabina == 3 or pais_de_la_cabina == 4:
    importe_basico = 300
elif pais_de_la_cabina == 2:
    importe_basico = 400
elif pais_de_la_cabina == 1:
    importe_basico = 200


# Ajuste de importe BASE segun tipo de vehículo. Se obtiene el Importe BASICO
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
print(f"Importe básico para el vehículo: $ {importe_basico}")
print(f"Valor final del ticket: $ {valor_final_del_ticket}")

if distancia > 0:
    promedio = valor_final_del_ticket/distancia
    print ("Valor promedio pagado por el vehículo por cada kilómetro recorrido: $", round(promedio,2))
else:
    print ("No aplica el cálculo de valor promedio por kilómetro")
"""