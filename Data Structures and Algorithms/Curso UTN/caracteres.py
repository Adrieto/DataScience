def es_letra(car):
    return car.isalpha()

def es_digito(car):
    return "0" <= car <= "9"

def es_valido(car):
    return es_letra(car) or es_digito(car)

def es_separador(car):
    return not es_valido(car)

def es_vocal(car):
    return car.lower() in "aeiouáéíóú"

def es_consonante(car):
    return car.isalpha() and not es_vocal(car)

def es_minuscula(car):
    return car == car.lower()