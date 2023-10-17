class Alumno:
    def __init__(self, dni, nombre, apellido, dni_tutor, cuota, nivel):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.dni_tutor = dni_tutor
        self.cuota = cuota
        self.nivel = nivel

    def __str__(self):
        return f"{self.dni:<9} {self.nombre:<12} {self.apellido:^10} {self.dni_tutor:<9} {self.cuota:>8} {self.nivel:3}"

