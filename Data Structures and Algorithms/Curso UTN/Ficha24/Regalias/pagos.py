# 3. Pagos Regalías
# Una empresa dedicada al cobro de regalias de la industria audiovisual no ha solicitado un programa que permita cargar
# los pagos que le debe realizar a sus clientes. Para ellos se sabe que un pago esta conformado por la siguiente información:
#   * Numero (string)
#   * Nombre del cliente (string)
#   * Tipo de Empleo (0 - Director, 1 - Productor, 2 - Maquillador, 3 - Actor, 4 - Asistentes, 5 - Especialista CGI, 6 - Vestuarista)
#   * Tipo de Producto (1 - Pelicula, 2 - Serie, 3 - Documental, 4 - Videojuego, 5 - Corto Animación)
#   * Monto a Pagar (float)
#   * Gastos a Cobrar (float)

TIPO_EMPLEO = ("Director", "Productor", "Maquillador", "Actor", "Asistentes", "Especialista CGI", "Vestuarista")
TIPO_PRODUCTO = ("Pelicula", "Serie", "Documental", "Videojuego", "Corto Animación")

class Pago:
    def __init__(self, numero, nombre, empleo, producto, monto_pagar, gastos_cobrar):
        self.numero = numero
        self.nombre = nombre
        self.empleo = int(empleo)
        self.producto = int(producto)
        self.monto_pagar = float(monto_pagar)
        self.gastos_cobrar = float(gastos_cobrar)

    def __str__(self):
        return f"{self.numero}, {self.nombre}, {TIPO_EMPLEO[self.empleo]}, {TIPO_PRODUCTO[self.producto-1]}, {self.monto_pagar}, {self.gastos_cobrar}"

    def csv(self):
        return f"{self.numero}, {self.nombre}, {TIPO_EMPLEO[self.empleo]}, {TIPO_PRODUCTO[self.producto-1]}, {self.monto_pagar}, {self.gastos_cobrar}\n"