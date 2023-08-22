def es_vocal(car):
    return car.lower() in "aeiouáéíóú"

def es_consonante(car):
    return car.isalpha() and not es_vocal(car)

def promedio_entero(total, n):
    if n > 0:
        return total//n
    return 0



def test():
    archivo = open("entrada simulacro 2.txt")
    texto = archivo.readline()
    archivo.close()

    # Contadores
    r1 = r2 = r3 = r4 = 0
    cl = 0
    contador_punto3 = 0
    cont_vocales = cont_consonantes = cont_palabras_totales = 0

    # Banderas
    bandera_digit = bandera_p = bandera_s = False
    bandera_r = bandera_ra = bandera_vocal = False

    # Acumuladores
    acumulador_punto3 = 0



    for car in texto:

        if car not in " .":
            cl += 1

            # Punto 1
            if es_vocal(car):
                cont_vocales += 1
            elif es_consonante(car):
                cont_consonantes += 1

            # Punto 2
            if car.isdigit():
                bandera_digit = True
            elif car in "pP":
                bandera_p = True

            # Punto 3
            if car in "sS":
                bandera_s = True

            # Punto 4
            if es_vocal(car) and cl <= 2:
                bandera_vocal = True
            if car in "rR":
                bandera_r = True
            elif car in "aA" and bandera_r:
                bandera_ra = True
            else:
                bandera_r = False





        else:
            if cl > 0:
                cont_palabras_totales += 1

            # Punto 1
            if cl % 2 == 0 and cont_vocales == cont_consonantes:
                r1 += 1

            # Punto 2
            if bandera_digit and not bandera_p and cl > r2:
                r2 = cl

            # Punto 3
            if bandera_s and cl > 2:
                acumulador_punto3 += cl
                contador_punto3 += 1

            # Punto 4
            if bandera_ra and bandera_vocal:
                r4 += 1


            # Reinicios
            cl = 0
            cont_vocales = cont_consonantes = 0
            bandera_digit = bandera_p = bandera_s = bandera_r = bandera_ra = False
            bandera_vocal = False


    r3 = promedio_entero(acumulador_punto3, contador_punto3)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    test()