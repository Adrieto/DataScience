class Venta:
    def __init__(self, numero_factura, importe, tipo_factura, apellido, tipo_perfume):
        self.numero_factura = numero_factura
        self.importe = importe
        self.tipo_factura = tipo_factura
        self.apellido = apellido
        self.tipo_perfume = tipo_perfume

    def __str__(self):
        return f"Nro: {self.numero_factura}, ${self.importe}, Tipo: {self.tipo_factura}, {self.apellido}, " \
               f"perfume: {self.tipo_perfume}"