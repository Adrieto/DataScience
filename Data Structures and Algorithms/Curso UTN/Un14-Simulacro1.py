"""1. Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas. Por ejemplo, en el texto: “La clave 1alfaxy puede funcionar en lugar
de 1beta9 o en lugar de 9sigmaZ.” hay solo una palabra que cumple: “1alfaxy”.

2. Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que comienzan
con una vocal y contenga al menos una letra ‘b’ (mayúscula o minúscula). Por ejemplo, en el texto: “Antes de
esa esperada circunstancia era imposible.” la mayor longitud entre las palabras que comienzan con vocal es
de 9 caracteres (en la palabra “imposible”). Note que la palabra “circunstancia” tiene más de 9 caracteres,
pero no comienza con vocal, por lo que no debe ser considerada.

3. Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más consonantes que
vocales, pero no contienen ninguna ‘m’ ni tampoco ninguna ‘a’. Por ejemplo, en el texto “Secos los pozos entre
tantas mejoras.” hay cuatro palabras que cumplen el criterio: “Secos”, “los”, “pozos” y “entre”, y suman 18
caracteres entre todas ellas. Por lo tanto, el promedio entero pedido es de 4 letras por palabra.

4. Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra “d” mas una vocal
(con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la palabra termine además con una
vocal. Por ejemplo, en el texto: “La dadiva va a ser dividida dijo el pastor.” hay dos palabras que cumplen:
“dadiva” y “dividida”. La palabra “dijo” no cuenta porque solo tiene una vez la expresión “d” + vocal. """

from Un13_Ej9.funciones import procesamiento_palabras
from caracteres import *


def promedio_entero(total, cantidad):
    return total // cantidad


def test():
    archivo = open ("entrada.txt")
    texto = archivo.readline()
    print(texto)
    print(type(texto))

    # Contadores
    cont_letras = cont_empieza_con_impar = cont_palabras_totales = longitud = 0
    cont_vocal = cont_consonante = cont_palabras_sin_a_m = 0
    cont_d_mas_vocal = cont_palabras_d_mas_vocal = 0

    #Acumuladores
    acum_letras = 0

    # Banderas
    empieza_con_impar_minusculas = empieza_con_vocal = bandera_contiene_b = False
    bandera_m_a = bandera_d_mas_vocal = False
    bandera_es_vocal = False

    for car in texto:

        if es_valido(car):
            cont_letras += 1

            if es_vocal(car):
                bandera_es_vocal = True
            else:
                bandera_es_vocal = False

            if es_digito(car) and int(car) % 2 == 1 and cont_letras == 1:
                empieza_con_impar_minusculas = True

            elif not es_minuscula(car):
                empieza_con_impar_minusculas = False

            if car in "bB":
                bandera_contiene_b = True

            if bandera_es_vocal and cont_letras == 1:
                empieza_con_vocal = True

            if car not in 'aAmM':
                if es_vocal(car):
                    cont_vocal += 1
                elif es_consonante(car):
                    cont_consonante += 1

            if car in "dD":
                bandera_d_mas_vocal = True
            else:
                if bandera_es_vocal and bandera_d_mas_vocal:
                    cont_d_mas_vocal += 1
                bandera_d_mas_vocal = False


        else:
            if cont_letras > 0:
                cont_palabras_totales += 1
            if empieza_con_impar_minusculas:
                cont_empieza_con_impar += 1
            if empieza_con_vocal and bandera_contiene_b and cont_letras > longitud:
                longitud = cont_letras
            if not bandera_m_a and cont_consonante > cont_vocal:
                acum_letras += cont_letras
                cont_palabras_sin_a_m += 1
            if cont_d_mas_vocal >= 2 and bandera_es_vocal:
                cont_palabras_d_mas_vocal += 1



            # Reinicios
            bandera_contiene_b = empieza_con_vocal = empieza_con_impar_minusculas = False
            bandera_m_a = bandera_d_mas_vocal = bandera_es_vocal = False
            cont_letras = cont_d_mas_vocal = 0



    print(f"Palabras totales: {cont_palabras_totales}")
    print(f"Cantidad de palabras que comienzan con digito impar y el resto son minusculas: {cont_empieza_con_impar}")
    print(f"Longitud de palabra mas larga que comienza con vocal y contiene la letra b: {longitud}")
    print(f"Promedio de palabras con mas consonantes que vocale y sin letras 'm' o 'a': "
          f"{promedio_entero(acum_letras, cont_palabras_sin_a_m)}")
    print(f"Palabras que contiene 'd+vocal' 2 ò mas veces y terminan en vocal: {cont_palabras_d_mas_vocal}")



if __name__ == "__main__":
    test()