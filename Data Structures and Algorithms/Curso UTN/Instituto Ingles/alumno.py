import random

class Alumno:
    def __init__(self, dni, nombre, apellido, dni_tutor, importe, nivel):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.dni_tutor = dni_tutor
        self.importe = importe
        self.nivel = nivel

    def __str__(self):
        return f'{self.dni:^10} {self.nombre:<15} {self.apellido:^10} {self.dni_tutor:^10} {self.importe:>10} {self.nivel:5}'

def encabezado():
    sep = '=' * 75
    cadena = f'| {"DNI":^10} | {"Nombre":^15} | {"Apellido":^10} | ' \
             f'{"Dni Tutor":^10} | ${"Importe":^10} | {"Nivel":^5} |\n{sep:<75}'
    titulo = f'{sep:<75}\n|{"Listado de Alumnos":^73}|\n{sep:<75}\n{cadena:<75}'
    return titulo


def carga_aleatoria(vector, n):
    nombres = ['Daiana', 'Zulma', 'Diego', 'Federico', 'Matias', 'Juan', 'Elena', 'Azul', 'Julian', 'Joaquin',
               'Marcelo']
    apellidos = ['Makula', 'Serrano', 'Vasquievich', 'Avalos', 'Perez', 'Gonzalez', ' Rodriguez', 'Alvarez', 'Vega']
    for i in range(n):
        dni = random.randint(1000000, 50999999)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        dni_tutor = random.randint(1000000, 41999999)
        importe = round(random.uniform(7000, 15000), 2)
        nivel = random.randint(1, 10)
        alumno = Alumno(dni, nombre, apellido, dni_tutor, importe, nivel)
        vector.append(alumno)
