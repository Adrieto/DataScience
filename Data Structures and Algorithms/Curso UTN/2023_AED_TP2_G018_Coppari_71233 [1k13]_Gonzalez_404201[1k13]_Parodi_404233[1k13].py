# TP2 Patentes y peajes
# Formatos posibles:

# Argentina: LLNNNLL     "AK348LZ"
# Bolivia:   LLNNNNN     "AP85986"
# Brasil:    LLLNLNN     "ASF5Q99"
# Paraguay:  LLLLNNN     "ASFQ849"
# Uruguay:   LLLNNNN     "ASF8492"
# Chile:      LLLLNN     " LANY87"
# Otro:      Cualquier otro formato

archivo = open("peajes.txt")
lines = archivo.readlines()
archivo.close()

# Contadores
carg = cbol = cbra = cchi = cpar = curu = cotr = disAB = cantAB = 0
distancia_carg_por_brasil = 0
cdpp = 0 #Frecuencia de aparicion
cpp = 0 #Frecuencia de aparicion primera patente

# Acumuladores
imp_acu_total = 0

# Otros
mayimp = 0
maypat = None

# Deteccion de idioma:
if "PT" in lines[0]:
    idioma = "Portugués"
elif "ES" in lines[0]:
    idioma = "Español"


lines = lines[1:]      # Encabezado elimindado --> Lineas con patentes

for line in lines:
    patente = line[0:7]
    tipo_de_vehiculo = int(line[7])
    forma_de_pago = int(line[8])
    pais_de_la_cabina = int(line[9])
    distancia = int(line[10:-1])
    #print(line)
    #print(f"{patente} + {tipo_vehiculo} + {forma_pago} + {pais_procedencia} + {kms}")

    # Vehículos por país
    # Chequeamos el origen de las patentes:
    if len(patente) == 7 and patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
        pais_procedencia = "Argentina"
        carg += 1
    elif len(patente) == 7 and patente[0:2].isalpha() and patente[2:7].isdigit():
        pais_procedencia = "Bolivia"
        cbol += 1
    elif (
        len(patente) == 7
        and patente[0:3].isalpha()
        and patente[3].isdigit()
        and patente[4].isalpha()
        and patente[5:7].isdigit()
    ):
        pais_procedencia = "Brasil"
        cbra += 1
    elif len(patente) == 7 and patente[0:4].isalpha() and patente[4:7].isdigit():
        pais_procedencia = "Paraguay"
        cpar += 1
    elif len(patente) == 7 and patente[0:3].isalpha() and patente[3:7].isdigit():
        pais_procedencia = "Uruguay"
        curu += 1
    elif len(patente) == 7 and patente[0] == " " and patente[1:5].isalpha() and patente[5:7].isdigit():
        pais_procedencia = "Chile"
        cchi += 1
    else:
        pais_procedencia = "Otro"
        cotr += 1

    # Pais en donde se encuentra la cabina de peaje
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

    # Se establece el importe BASE según país
    if pais_de_la_cabina == 0 or pais_de_la_cabina == 3 or pais_de_la_cabina == 4:
        importe_base = 300
    elif pais_de_la_cabina == 2:
        importe_base = 400
    elif pais_de_la_cabina == 1:
        importe_base = 200

    # Ajuste de importe BASE segun tipo de vehículo. Se obtiene el Importe BASICO
    if tipo_de_vehiculo == 0:
        importe_basico = 0.5 * importe_base
    elif tipo_de_vehiculo == 2:
        importe_basico = 1.6 * importe_base
    else:
        importe_basico = importe_base

    # Importe final del ticket, según forma de pago
    if forma_de_pago == 2:
        importe_final_del_ticket = importe_basico - (0.1 * importe_basico)
    else:
        importe_final_del_ticket = importe_basico

    # Mayor importe final de ticket y patente de ese ticket
    if importe_final_del_ticket > mayimp:
        mayimp = importe_final_del_ticket
        maypat = patente

    imp_acu_total += importe_final_del_ticket

    # Cantidad de patentes procesadas (4)
    if patente:
        cdpp += 1
        if cdpp == 1:
            primera = patente
        if patente == primera:
            cpp += 1

    # Cantidad de vehículos de Argentina en la cabina de Brasil y la distancia que recorrieron
    if pais_procedencia == "Argentina" and pais_de_la_cabina == 2:
        disAB += distancia
        cantAB += 1


porc = round(cotr * 100 / cdpp, 2)

if cantAB != 0:
    prom = round(disAB / cantAB, 2)
else:
    prom = 0

# Visualicación de resultados...
print()
print('(r1) - Idioma a usar en los informes:', idioma)
print()
print('(r2) - Cantidad de patentes de Argentina:', carg)
print('(r2) - Cantidad de patentes de Bolivia:', cbol)
print('(r2) - Cantidad de patentes de Brasil:', cbra)
print('(r2) - Cantidad de patentes de Chile:', cchi)
print('(r2) - Cantidad de patentes de Paraguay:', cpar)
print('(r2) - Cantidad de patentes de Uruguay:', curu)
print('(r2) - Cantidad de patentes de otro país:', cotr)

print()
print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)

print()
print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición:', cpp)

print()
print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:', maypat)

print()
print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

print()
print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando porcabinas brasileñas:', prom, '\bkm')
