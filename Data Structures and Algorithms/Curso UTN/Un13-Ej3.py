from caracteres import *

texto = "pro89ksbanlado texto s4p2aa32qweaaarout87 abra2cada9bra lelilolu luciernaga."

#Contadores y acumuladores
largo = mas_largo = posicion_digito = 0
cont_palabras_totales = cont_termina_vocal = 0
cont_palabras_lv = cont_dig_menos_mitad = cont_pal_suma10 = 0
total_letras = 0
orden = 0
suma = 0

#Banderas
band_ult_vocal = band_suma10 = band_L = band_LV = False

for car in texto:
    if es_valido(car):
        largo += 1

        if es_vocal(car):
            band_ult_vocal = True
        else:
            band_ult_vocal = False

        if car in "lL":
            band_L = True
        else:
            if band_ult_vocal and band_L:
                band_LV = True
            band_L = False

        if es_digito(car) and posicion_digito == 0:
            posicion_digito = largo

        if es_digito(car):
            suma += int(car)
            if suma >= 10 and band_suma10 is False:
                posicion = largo
                band_suma10 = True

    else:
        if largo > 0:
            cont_palabras_totales += 1
            total_letras += largo

        if band_ult_vocal:
            cont_termina_vocal += 1

        if largo > mas_largo:
            orden = cont_palabras_totales
            mas_largo = largo

        if band_LV:
            cont_palabras_lv += 1
            band_LV = False

        mitad = largo // 2

        if posicion_digito <= mitad and posicion_digito != 0:
            cont_dig_menos_mitad += 1

        if 0 < posicion <= mitad:
            cont_pal_suma10 += 1

        # Reinicios cuando termina una palabra
        band_ult_vocal = band_suma10 = False
        posicion_digito = suma = largo = posicion = 0

# Calculos e imprimir en pantalla:
print (texto)
print (f"Palabras totales: {cont_palabras_totales}")
print (f"Cant de palabras terminan en vocal: {cont_termina_vocal}")
print(f"Palabra mas larga en posicion {orden}. Contiene {mas_largo} caracteres")
print(f"Cant de palabras con 'L+vocal': {cont_palabras_lv}")
print(f"Cant palabras con algun digito antes de la mitad: {cont_dig_menos_mitad}")
print(f"Cant palabras con digitos cuya suma sea mayor a 10 en su primer mitad: {cont_pal_suma10}")



