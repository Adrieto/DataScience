
def es_vocal(car):
    return car.lower() in "aeiouáéíóú"

def es_consonante(car):
    return not es_vocal(car) and not car.isdigit()


def test():
    archivo = open ("entrada.txt")
    texto = archivo.readline()
    archivo.close()

    # Contadores
    cl = cont_palabras_totales = cont_vocales = cont_consonantes = 0
    cont_punto1 = cont_punto3 = longitud = cont_punto4 = 0

    # Banderas
    bandera_digito = bandera_p = bandera_s = bandera_vocal = False
    bandera_ra = bandera_r = False

    # Acumuladores
    acumuluador3 = 0

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
                bandera_digito = True
            if car in "pP":
                bandera_p = True

            # Punto 3
            if car in "sS":
                bandera_s = True

            # Punto 4
            if es_vocal(car) and cl <= 2:
                bandera_vocal = True
            if car in "rR":
                bandera_r = True
            elif bandera_r and car in "aA":
                bandera_ra = True
            else:
                bandera_r = False

        else:
            if cl > 0:
                cont_palabras_totales += 1

            # Punto 1
            if cl % 2 == 0 and cont_vocales == cont_consonantes:
                cont_punto1 += 1

            # Punto 2
            if bandera_digito and not bandera_p and cl > longitud:
                longitud = cl
            # Punto 3
            if cl > 2 and bandera_s:
                acumuluador3 += cl
                cont_punto3 += 1

            # Punto 4
            if bandera_ra and bandera_vocal:
                cont_punto4 += 1


            # Reinicios
            cl = cont_vocales = cont_consonantes = 0
            bandera_p = bandera_digito = bandera_s = bandera_ra = bandera_r = False

    if cont_punto3 > 0:
        promedio3 = acumuluador3 // cont_punto3
    else:
        promedio3 = 0

    print (f"resultado punto 1: {cont_punto1} ")
    print (f"resultado punto 2: {longitud}")
    print (f"resultado punto 3: {promedio3}. caracteres={acumuluador3}, palabras={cont_punto3}")
    print (f"resultado punto 4: {cont_punto4}")










if __name__ == "__main__":
    test()



