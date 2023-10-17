# 3. (Parcial 2021) - La Perfumeria
# Una perfumería desea un programa que procese los datos de las ventas que realiza. En cada Venta se registran
# los siguientes datos: el número de factura, importe de la factura, el tipo de factura (A, B, C o E), el apellido
# de la persona que realiza la compra, y el tipo del perfume vendido (un número entero para indicar su marca,
# entre 1 y 17, por ejemplo: 1: Chanel, 2: Paco Rabanne, etc.). Se desea almacenar la información referida a las
# ventas que realiza la perfumería en un arreglo de registros de tipo Venta (definir el tipo Venta y cargar n por teclado).

class Venta:
    def __init__(self, numero, importe, factura, apellido, tipo_perfume):
        self.numero = numero
        self.importe = importe
        self.factura = factura
        self.apellido = apellido
        self.tipo_perfume = tipo_perfume

    def __str__(self):
        return f"{self.numero}, ${self.importe}, {self.factura}, {self.apellido}, {self.tipo_perfume}"