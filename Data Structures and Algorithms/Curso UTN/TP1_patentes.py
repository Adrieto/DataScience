# TP1 Patentes y peajes
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
# patente = "ASF8492"  # Uru
patente = "1" # Otro

<<<<<<< HEAD
# Chequeamos que el origen de las patentes:
if len(patente) == 7 and patente[0:2].isalpha() and patente[2:5].isdecimal() and patente[5:7].isalpha():
    pais_procedencia = "Argentina"
elif len(patente) == 7 and patente[0:2].isalpha() and patente[2:7].isdecimal():
    pais_procedencia = "Bolivia"
elif (
    len(patente) == 7
    and patente[0:3].isalpha()
    and patente[3].isdecimal()
=======
if patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
    pais_procedencia = "Argentina"
elif patente[0:2].isalpha() and patente[2:7].isdigit():
    pais_procedencia = "Bolivia"
elif (
    patente[0:3].isalpha()
    and patente[3].isdigit()
>>>>>>> 7aa319db4511588a7e59c7479d6a70effc75910f
    and patente[4].isalpha()
    and patente[5:7].isdigit()
):
    pais_procedencia = "Brasil"
<<<<<<< HEAD
elif len(patente) == 7 and patente[0:4].isalpha() and patente[4:7].isdecimal():
    pais_procedencia = "Paraguay"
elif len(patente) == 7 and patente[0:3].isalpha() and patente[3:7].isdecimal():
=======
elif patente[0:4].isalpha() and patente[4:7].isdigit():
    pais_procedencia = "Paraguay"
elif patente[0:3].isalpha() and patente[3:7].isdigit():
>>>>>>> 7aa319db4511588a7e59c7479d6a70effc75910f
    pais_procedencia = "Uruguay"
else:
    pais_procedencia = "Otro"

print(pais_procedencia)
