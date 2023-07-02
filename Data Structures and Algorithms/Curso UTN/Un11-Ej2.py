"""2. Sílaba 'li'
Se solicita crear un programa que permita ingresar un texto, las palabras se encontraran
 separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto.
  En base a ese texto determinar:

a) Cantidad de palabras que comienzan con consonantes y terminan en vocales
b) Cantidad de palabras que poseen la secuencia ‘li’ a partir de la tercera letra de la palabra
c) Cantidad de palabras con menos de 4 letras y porcentaje que dicha cantidad representa
sobre el total del texto
"""

def es_vocal(car):
    vocales = "aeiou"
    return car.lower() in vocales


#texto = input("ingrese texto (termine con punto): ")
texto = " Era Hola constant ss mundo sos habiladli plina"
#texto = "habilidad"
if texto[-1]!= ".":
    texto += "."

# Variables palabras:
cl = 0
cp = 0
cont_pal_empieza_consonante_termina_vocal = 0
palabras_menosd_de_4_letras = 0
empieza_con_consonante = False
anterior_es_vocal = False
anterior_es_l = False
tiene_li = False
contador_li = 0

for car in texto:
    cl += 1

    # Es el fin de la palabra?
    if car == " " or car == ".":
        if cl > 1:
            cp += 1

            if cl < 5:
                palabras_menosd_de_4_letras += 1
            if empieza_con_consonante and anterior_es_vocal:
                cont_pal_empieza_consonante_termina_vocal += 1
            if tiene_li:
                contador_li += 1


        # Reinicio
        cl = 0
        empieza_con_consonante = False
        tiene_li = False
        anterior_es_l = False

    else:
        #Proceso la letra
        # Primer caracter de la palabra es vocal?:
        if cl == 1 and not es_vocal(car):
            empieza_con_consonante = True

        if es_vocal(car):
            anterior_es_vocal = True
        else:
            anterior_es_vocal = False

        if car in "lL":
            anterior_es_l = True

        elif anterior_es_l and cl >= 4 and car in "iI":
            tiene_li = True
        else:
            anterior_es_l = False


print (texto)
print (f"Palabras que empiezan con cons y terminan en vocal: {cont_pal_empieza_consonante_termina_vocal}")
print(f"Palabras totales: {cp}")
print(f"Palabras con LI a partir de la tercera letra: {contador_li}")
print(f"cantidad de palabras de menos de 4 letras: {palabras_menosd_de_4_letras}. Porcentaje: {palabras_menosd_de_4_letras / cp}")