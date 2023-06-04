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

