""" 7. Enunciado tipo Parcial
Se pide desarrollar un programa en Python que permita cargar desde un achivo de textos llamado 'entrada.txt'
(click aquí para ver y descargar ese archivo) un texto completo en una variable de tipo cadena de caracteres.
El texto en el archivo finaliza con ‘.’ y cada palabra de ese texto está separada de las demás por un espacio
en blanco. El programa debe incluir una función principal para lanzar el programa, control de ejecución del
script principal con la variable __name__ y al menos una función simple con parámetros y retorno de resultado.
El programa debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo, con un único ciclo
para todo el proceso), y debe hacer lo siguiente sin usar un menú de opciones:

1. Determine la cantidad de palabras que contengan una consonante en la 3 o 5 letra de la palabra y que finalice
con un vocal.

2. Determine la cantidad de palabras que contienen al menos un dígito y que son de longitud impar.

3. Determinar el promedio entero de caracteres por palabra entre las palabras que contiene al menos una letra 't'
y un letra 's' la cual debe aparecer después de la 't'.

4. Determinar cuantas palabras incluyen la expresión "ma" a partir de la cuarta letra de la palabra y contengan
la primera letra del texto.
"""

def es_vocal(car):
    return car.lower() in "aeiouáéíóú"

def es_consonante(car):
    return car.isalpha() and not es_vocal(car)


def test():
    #Apertura de archivo
    archivo = open("entrada14-7.txt")
    texto = archivo.readline()


    # Contadores
    cl = cont_punto1 = cont_punto2 = cont_punto3 = cont_punto4 = cont_palabras_totales = 0

    # Acumuladores
    acum_punto3 = 0

    # Banderas
    bandera_vocal = bandera_punto1 = bandera_digito = bandera_t = bandera_ts = False
    bandera_m = bandera_ma = bandera_primera = False


    for car in texto:

        if car not in " .":
            cl += 1

            # Punto 1:
            if es_vocal(car):
                bandera_vocal = True
            else:
                bandera_vocal = False

            if (cl == 3 or cl == 5) and es_consonante(car):
                bandera_punto1 = True

            # Punto 2:
            if car.isdigit():
                bandera_digito = True


            # Punto 3
            if car in "tT":
                bandera_t = True
            elif car in "sS" and bandera_t:
                bandera_ts = True
            else:
                bandera_t = False

            # Punto 4

            if cl == 1 and cont_palabras_totales == 0:
                primera_letra = car

            if car == primera_letra:
                bandera_primera = True

            if car in "mM" and cl >= 4:
                bandera_m = True
            elif car in "aA" and bandera_m:
                bandera_ma = True
            else:
                band_m = False

        else:

            if cl > 0:
                cont_palabras_totales += 1

            # Punto 1:
            if bandera_punto1 and bandera_vocal:
                cont_punto1 += 1

            # Punto 2:
            if bandera_digito and cl % 2 == 1:
                cont_punto2 += 1

            # Punto 3:
            if bandera_ts:
                acum_punto3 += cl
                cont_punto3 += 1

            # Punto 4:
            if bandera_primera and bandera_ma:
                cont_punto4 += 1

            #Reinicios
            cl = 0
            bandera_punto1 = bandera_digito = bandera_t = bandera_ts = False
            bandera_m = bandera_ma = bandera_primera = False

    if cont_punto3 > 0:
        promedio_punto_3 = acum_punto3 / cont_punto3
    else:
        promedio_punto_3 = 0

    print(f"Resultado 1: {cont_punto1}")
    print(f"Resultado 2: {cont_punto2}")
    print(f"Resultado 3: {promedio_punto_3}")
    print(f"Resultado 4: {cont_punto4}")


if __name__ == "__main__":
    test()




