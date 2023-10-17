# Una empresa agropecuaria necesita un programa para procesar los datos de los trabajos ofrecidos.
# Por cada trabajo se tienen los siguientes datos: el número de identificación, la descripción del trabajo,
# el tipo de trabajo (un número entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas,
# 2: cosecha, etc.), el importe a cobrar por ese trabajo y la cantidad de personal afectado al mismo. Se desea
# almacenar la información referida a estos trabajos en un arreglo de registros de tipo Trabajo (definir el tipo
# Trabajo y cargar n por teclado).


class Trabajo:
    def __init__(self, idenficacion, descripcion, tipo_trabajo, importe, personal_afectado):
        self.identificacion = idenficacion
        self.descripcion = descripcion
        self.tipo_trabajo = tipo_trabajo
        self.importe = importe
        self.personal_afectado = personal_afectado

    def __str__(self):
        return f"Identificacion: { self.identificacion}, Descripcion: {self.descripcion}, Tipo de trabajo: {self.tipo_trabajo}, Importe: ${self.importe}, Personal afectado: {self.personal_afectado}"
