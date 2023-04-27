# Pruebas para el TP 1 de las patentes
# Formatos:

# Argentina: LLNNNLL
# Bolivia:   LLNNNNN
# Brasil:    LLLNLNN
# Paraguay:  LLLLNNN
# Uruguay:   LLLNNNN


# patente = "AK348LZ" # Arg
# patente = "AP85986" # Bol
# patente = "ASF5Q99" # Bra
# patente = "ASFQ849" # Par
patente = "ASF8249"  # Uru

if patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
    pais_procedencia = "Argentina"
elif patente[0:2].isalpha() and patente[2:7].isdigit():
    pais_procedencia = "Bolivia"
elif (
    patente[0:3].isalpha()
    and patente[3].isdigit()
    and patente[4].isalpha()
    and patente[5:7].isdigit()
):
    pais_procedencia = "Brasil"
elif patente[0:4].isalpha() and patente[4:7].isdigit():
    pais_procedencia = "Paraguay"
elif patente[0:3].isalpha() and patente[3:7].isdigit():
    pais_procedencia = "Uruguay"
else:
    pais_procedencia = "Otro"

print(pais_procedencia)
