"""9. Ejercicio Proceso de Cadenas.
Procesar un texto que se ingresa por teclado, en el texto las palabras están separadas
 por uno o más espacios en blanco y el texto finaliza con un ".".
El programa debe estar organizado en funciones y el script principal solo puede contener
 una llamada a una función para iniciar el programa. El texto se debe procesar de a una
  letra por vez (es decir una letra por vuelta de ciclo). En base a los lineamientos
   anteriores el programa debe determinar:

1 - Determinar el porcentaje de palabras con más vocales que consonantes.
2 - Determinar la cantidad de caracteres de la palabra con menor cantidad de caracteres del texto.
3 - Determinar cantidad de palabras que tuvieron al menos una vez la secuencia 'sa' o 'se' o 'si' o 'so' o 'su'.
4 - Determinar la cantidad de palabras que comenzaron con el último caracter de la palabra anterior."""

from funciones.procesamiento_palabras import *

def test():

    #texto = input ("ingrese texto, termine con un '.': ")
    texto = "cosoo OHola Mundo obala ser air y yesos sossos."

    # Contadores
    cont_caracateres = cont_vocal = cont_consonante = cont_palabras_totales = 0
    cont_mas_vocales = cont_s_vocal = 0
    cont_palabras_punto4 = 0
    min_caracteres = 10000

    # Banderas
    bandera_s = bandera_s_vocal = False
    bandera_fin_palabra = False

    # Otros
    ultimo_caracter = None

    for car in texto:
        if es_vocal(car) or es_consonante(car):
            cont_caracateres += 1

            if es_vocal(car):
                cont_vocal += 1
            elif es_consonante(car):
                cont_consonante += 1

            if car in "sS":
                bandera_s = True

            elif bandera_s and es_vocal(car):
                bandera_s_vocal = True

                bandera_s = False

            if bandera_fin_palabra and car.lower() == ultimo_caracter:
                cont_palabras_punto4 += 1
            else:
                ultimo_caracter = car.lower()

            bandera_fin_palabra = False

        else:
            if cont_caracateres > 0:
                cont_palabras_totales += 1

            if cont_vocal > cont_consonante:
                cont_mas_vocales += 1

            if min_caracteres > cont_caracateres > 0:
                min_caracteres = cont_caracateres

            if bandera_s_vocal:
                cont_s_vocal += 1

            bandera_fin_palabra = True

            #Reinicios:
            bandera_s = bandera_s_vocal = False
            cont_consonante = cont_vocal = cont_caracateres = 0

    porcentaje_con_mas_vocales = cont_mas_vocales * 100 / cont_palabras_totales
    print(f"Porcentaje de palabras con mas vocales que consonantes: {porcentaje_con_mas_vocales}")
    print(f"Numero de caracteres en la palabra con menos letras: {min_caracteres}")
    print(f"Palabras totales: {cont_palabras_totales}")
    print(f"Palabras con S+VOCAL: {cont_s_vocal}")

    print(f"Cantidad de palabras que empiezan con la letra con la que terminó la palabra anterior: {cont_palabras_punto4}")

# Script principal
if __name__ == "__main__":
    test()
