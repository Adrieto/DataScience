from TP3.ticket import *

class Prueba():
    def __init__(self, identificador,patente):
        self.identificador = identificador
        self.patente = patente
        self.pais = self.pais_de_patente()

    def __str__(self):
        #r = str(self.identificador) + " Es el identificador y " + str(self.patente) + "la patente"
        r = f"{self.identificador} es el identificador y {self.patente} la patente. El pais es {self.pais}"
        return r

    def pais_de_patente(self):
        PAISES = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros")

        if len(self.patente) == 7 and self.patente[0:2].isalpha() and self.patente[2:5].isdigit() and self.patente[5:7].isalpha():
            return PAISES[0]

        elif len(self.patente) == 7 and self.patente[0:2].isalpha() and self.patente[2:7].isdigit():
            return PAISES[1]

ticketZ = Prueba(12548863, "AK348LZ")
print(ticketZ)



arreglo_tickets = []
archivo = "TP3/5peajes-tp3.txt"
arreglo_tickets = cargar_tickets_desde_archivo(archivo)
#mostrar_tickets_ordenados(arreglo_tickets)


