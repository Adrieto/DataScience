# Un club deportivo necesita procesar los pagos realizados por sus socios. Para ello, se cuenta con un archivo
# denominado cuotas.dat, donde cada registro contiene:
#
#   - Número de socio.
#   - Deporte que realiza (0: Natacion/1: Basquet/2: Karate/3: Futbol/ 4: Patin).
#   - Día del mes en que pagó.
#   - Valor de la cuota.
#   - Si el socio aún no abonó, el día del mes debe ser 0.

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

DEPORTES = ['Natacion', 'Basquet', 'Karate', 'Futbol', 'Patin']


class Cuota:
    def __init__(self, socio, deporte, dia, valor_cuota):
       self.socio = socio
       self.deporte = deporte
       self.dia = dia
       self.valor_cuota = valor_cuota

    def __str__(self):
       return f'{self.socio:<6} | {describir_deporte(self.deporte):<10} | {self.dia:>4} | ${self.valor_cuota:>5.2f}'

    def to_str_csv(self):
       return f'{self.socio:<8},{describir_deporte(self.deporte):<10},{self.dia:>4},{self.valor_cuota:>5.2f}'


def describir_deporte(deporte):
    return str(deporte) + '-' + DEPORTES[deporte]


def to_string_titulos():
    return '{:<6} | {:<10} | {:>4} | {:>8}'.format('Socio', 'Deporte', 'Dia', 'Valor')
