import random


class Paciente:
    def __init__(self, nro_historia, nombre, dias, cod_enfermedad):
        self.nro_historia = nro_historia
        self.nombre = nombre
        self.dias = dias
        self.cod_enfermedad = cod_enfermedad

    def __str__(self):
        return f"Nro historia: {self.nro_historia} - Nombre: {self.nombre} - Dias desde visita: {self.dias} - enfermedad:{self.cod_enfermedad}"

    def csv_string(self):
        return f"{self.nro_historia},{self.nombre},{self.dias},{self.cod_enfermedad}\n"


def cargar_paciente_random():
    nro = random.randint(1, 100000)
    nombre = random.choice(("Hugo", "Paco", "Luis"))
    fecha = random.randint(1, 100)
    cod = random.randint(0, 9)

    return Paciente(nro, nombre, fecha, cod)


def leer_csv(csv):
    # "34985,Pepe,59,6\n"
    # csv = csv[:-1]
    partes = csv.strip().split(",")
    nro = int(partes[0])
    nombre = partes[1]
    fecha = int(partes[2])
    cod = int(partes[3])
    return Paciente(nro, nombre, fecha, cod)


if __name__ == '__main__':
    x = cargar_paciente_random()
    print(x)
    print(x.csv_string())
    csv = "34985,Pepe,59,6\n"
    paciente = leer_csv(csv)
    print(paciente)
