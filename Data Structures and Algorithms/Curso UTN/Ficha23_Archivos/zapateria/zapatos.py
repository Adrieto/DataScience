# Desarrollar un programa controlado por menú de opciones para gestionar el catálogo de una zapatería.
# Por cada calzado se almacena código, talle y color. Se pide implementar las siguientes opciones:
class Zapato:
    def __init__(self, codigo, talle, color):
        self.codigo = codigo
        self.talle = talle
        self.color = color

    def __str__(self):
        return f"codigo: {self.codigo}, talle: {self.talle}, color: {self.color}"

