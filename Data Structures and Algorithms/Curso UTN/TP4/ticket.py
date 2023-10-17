class Ticket:
    PAISES = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros")

    def __init__(self, identificador, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia):
        self.identificador = int(identificador)
        self.patente = patente
        self.tipo_vehiculo = int(tipo_vehiculo)
        self.forma_pago = int(forma_pago)
        self.pais_cabina = int(pais_cabina)
        self.distancia = int(distancia)
        self.numero_pais = self.pais_de_patente()
        self.pais = self.PAISES[self.numero_pais]

    def __str__(self):
        r = f"{self.identificador: <10}  {self.patente}  {self.tipo_vehiculo}  {self.forma_pago}  {self.pais_cabina}  {self.distancia:>3}   PAIS: {self.pais}"
        return r

    def pais_de_patente(self):
        if len(self.patente) == 7 and self.patente[0:2].isalpha() and self.patente[2:5].isdigit() and\
                self.patente[5:7].isalpha():
            return 0
        elif len(self.patente) == 7 and self.patente[0:2].isalpha() and self.patente[2:7].isdigit():
            return 1
        elif len(self.patente) == 7 and self.patente[0:3].isalpha() and self.patente[3].isdigit() and \
                self.patente[4].isalpha() and self.patente[5:7].isdigit():
            return 2
        elif len(self.patente) == 7 and self.patente[0:4].isalpha() and self.patente[4:7].isdigit():
            return 3
        elif len(self.patente) == 7 and self.patente[0:3].isalpha() and self.patente[3:7].isdigit():
            return 4
        elif len(self.patente) == 7 and self.patente[0] == " " and self.patente[1:5].isalpha() and\
                self.patente[5:7].isdigit():
            return 5
        else:
            return 6


def abrir_archivo(nombre_archivo):
    """Abre un archivo y elimina su timestamp"""

    archivo = open(nombre_archivo)
    lines = archivo.readlines()
    archivo.close()
    lines = lines[1:]  # timestamp eliminado
    return lines


def lectura_datos(linea_texto):
    """Lee una linea del archivo previamente cargado y asigna porciones de esa linea a distintas variables"""

    codigo_identificador = linea_texto[0:10]
    patente = linea_texto[10:17]
    tipo_de_vehiculo = int(linea_texto[17])
    forma_de_pago = int(linea_texto[18])
    pais_de_la_cabina = int(linea_texto[19])
    distancia = int(linea_texto[20:-1])

    return codigo_identificador, patente, tipo_de_vehiculo, forma_de_pago, pais_de_la_cabina, distancia


def cargar_tickets_desde_archivo(archivo):
    lines = abrir_archivo(archivo)
    conjunto_tickets = []  # El arreglo se crea de cero cada vez
    for line in lines:
        identificador, patente, tipo_de_vehiculo, forma_de_pago, pais_de_la_cabina, distancia = lectura_datos(line)
        nuevo_ticket = Ticket(identificador, patente, tipo_de_vehiculo, forma_de_pago, pais_de_la_cabina,distancia)
        conjunto_tickets.append(nuevo_ticket)
    return conjunto_tickets


def cargar_ticket_por_teclado():
    identificador = validar_mayor(0, "Introduzca el codigo del ticket (mayor que 0): ")
    patente = input("Introduzca la patente: ")  # No requiere validacion. Solo verifacion de pais de procedencia.
    tipo_de_vehiculo = validar_entre(0, 2, "Introduzca el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    forma_de_pago = validar_entre(1, 2, "Introduzca forma de pago (1: manual, 2: telepeaje): ")
    pais_de_la_cabina = validar_entre(0, 4, "Ingrese el país donde se cobró el peaje (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")
    distancia = validar_mayor(0, "Indique los kilómetros recorridos desde la cabina anterior (mayor que 0):")
    nuevo_ticket = Ticket(identificador, patente, tipo_de_vehiculo, forma_de_pago, pais_de_la_cabina, distancia)
    return nuevo_ticket


def validar_entre(lim_inferior, lim_superior, mensaje):
    n = lim_inferior - 1
    while n < lim_inferior or n > lim_superior:
        n = int(input(mensaje))
        if n < lim_inferior or n > lim_superior:
            print(f"ERROR! El número debe estar entre {lim_inferior} y {lim_superior}")
    return n


def validar_mayor(limite, mensaje):
    n = limite - 1
    while n <= limite:
        n = int(input(mensaje))
        if n <= limite:
            print(f"ERROR! El número debe ser mayor que {limite}")
    return n
