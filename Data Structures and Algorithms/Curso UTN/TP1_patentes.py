# Pruebas para el TP 1 de las patentes
# Formatos:

# Argentina: LLNNNLL
# Bolivia:   LLNNNNN
# Brasil:    LLLNLNN
# Paraguay:  LLLLNNN
# Uruguay:   LLLNNNN


#patente = "AK348LZ" # Arg
#patente = "AP85986" # Bol
#patente = "ASF5Q99" # Bra 
#patente = "ASFQ849" # Par 
patente = "ASF8249" # Uru 

if  patente[0:2].isalpha() and patente[2:5].isdecimal() and patente[5:7].isalpha():
    print("patente argentina")
elif patente[0:2].isalpha() and patente[2:7].isdecimal():
    print("patente boliviana")
elif patente[0:3].isalpha() and patente[3].isdecimal() and patente[4].isalpha() and patente[5:7].isdecimal():
    print("patente brasilera")
elif patente[0:4].isalpha() and patente[4:7].isdecimal():
    print("patente paraguaya")
elif patente[0:3].isalpha() and patente[3:7].isdecimal():
    print("patente uruguaya")
else:
    print("Otra")
