class Pasaje:
    def __init__(self, pasaporte, nombre, destino, clase, monto):
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.destino = destino
        self.clase = clase
        self.monto = monto

    def __str__(self):
        return f"pasaporte: {self.pasaporte}, pasajero: {self.nombre}, destino: {DESTINOS[self.destino]}, clase: {self.clase}, monto: ${self.monto}"


DESTINOS = {100: "Bahamas", 101: "Bermudas", 102: "Puerto Rico", 103: "República Dominicana"}