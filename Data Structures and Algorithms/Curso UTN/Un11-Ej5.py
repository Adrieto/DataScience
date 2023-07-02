"""5. Sílaba "dre"
Desarrollar un programa en Python que permita cargar por teclado un texto completo.
Siempre se supone que el usuario cargará un punto para indicar el final del texto,
y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

a) Determinar cuántas palabras tenían exactamente 3 letras. OK
b) Determinar el porcentaje que las palabras del punto 1 representan en el total del palabras del texto. OK
c) Determinar cuántas palabras terminaban con la letra "s".
d) Determinar cuántas palabras contuvieron al menos una vez la expresión "dre". """



#texto = "Por favor derek decile a dr dre no te hagas del picante o sos boleta dragen."
texto = "edredon redro dedrerek draguen dre loco"

cont_letras = 0
cont_palabras_3_letras = 0
cont_palabras_totales = 0
cont_palabras_terminan_s = 0
cont_palabras_contiene_dre = 0

#flags
hay_letra_s = False
hay_d = hay_dr = hay_dre = False

for car in texto:
    cont_letras += 1

    if car == " " or car == ".":    #Termina palabra
        if cont_letras > 1:
            cont_palabras_totales += 1

        if cont_letras == 4:
            cont_palabras_3_letras += 1

        if hay_letra_s:
            cont_palabras_terminan_s += 1

        if hay_dre:
            cont_palabras_contiene_dre += 1
            hay_dre = False

        #Reinicio:
        cont_letras = 0

    else:        #proceso letra
        if car in "sS":
            hay_letra_s = True
        else:
            hay_letra_s = False

        if car in "Dd":
            hay_d = True
            hay_dr = False
        elif car in "rR" and hay_d:
            hay_dr = True
            #hay_d = False
        elif car in "eE" and hay_dr:
            hay_dre = True
        else:
            hay_dr = False
            hay_d = False

porcentaje_palabra_3_letras = cont_palabras_3_letras * 100 / cont_palabras_totales

print (f"Palabras totales: {cont_palabras_totales}")
print (f"Palabras con 3 letras: {cont_palabras_3_letras}. Porcentaje sobre el total: {porcentaje_palabra_3_letras}%")
print(f"Palabras que terminan en 's': {cont_palabras_terminan_s}")
print(f"Palabras que contienen 'dre': {cont_palabras_contiene_dre}")



