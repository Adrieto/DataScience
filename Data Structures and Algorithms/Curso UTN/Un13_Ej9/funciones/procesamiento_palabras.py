def es_vocal(car):
    if car.lower() in "aeiouáéíóú":
        return True
    return False


def es_consonante(car):
    if ("b" <= car.lower() <= "z" or car.lower() == "ñ") and not es_vocal(car):
        return True
    return False


