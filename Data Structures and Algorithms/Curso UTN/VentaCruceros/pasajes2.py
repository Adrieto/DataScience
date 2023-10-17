# Una empresa que vende cruceros, desea un programa para administrar la información de venta de pasajes.
# Por cada pasaje se conoce: pasaporte del pasajero (cadena de caracteres), nombre completo, código de destino
# (100: Bahamas, 101: Bermudas: 102: Puerto Rico, 103: República Dominicana), código de clase (un número entero
# entre 1 y 10, por ejemplo: 1: Clase Preferencial, 2: Clase superior, 3: Clase Turista, etc.) y el monto abonado
# por el pasaje. Se desea almacenar la información referida a los n pasajes en un arreglo de registros de tipo
# Pasaje (definir el tipo Pasaje y cargar n por teclado).

destinos = {100: "Bahamas", 101: "Bermudas", 102: "Puerto Rico", 103: "República Dominicana"}


class Pasaje:
    def __init__(self, pasaporte, nombre, cod_destino, cod_clase, monto):
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.cod_destino = cod_destino
        self.cod_clase = cod_clase
        self.monto = monto
        self.destino = destinos[self.cod_destino]

    def __str__(self):
        return f"Pasaporte: {self.pasaporte}, Nombre: {self.nombre}, Destino: {self.destino}," \
               f" Clase: {self.cod_clase}, Monto: ${self.monto}"




