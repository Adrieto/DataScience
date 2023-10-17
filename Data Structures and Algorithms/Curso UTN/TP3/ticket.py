PAISES = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros")


class Ticket:
    def __init__(
        self, identificador, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia
    ):
        self.identificador = int(identificador)
        self.patente = patente
        self.tipo_vehiculo = int(tipo_vehiculo)
        self.forma_pago = int(forma_pago)
        self.pais_cabina = int(pais_cabina)
        self.distancia = int(distancia)
        self.numero_pais = self.pais_de_patente()
        self.pais = PAISES[self.numero_pais]

    def __str__(self):
        r = f"{self.identificador: <10}  {self.patente}  {self.tipo_vehiculo}  {self.forma_pago}  {self.pais_cabina}  {self.distancia:>3}   PAIS: {self.pais}"
        return r

    def pais_de_patente(self):
        # PAISES = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros")

        if (
            len(self.patente) == 7
            and self.patente[0:2].isalpha()
            and self.patente[2:5].isdigit()
            and self.patente[5:7].isalpha()
        ):
            return 0

        elif (
            len(self.patente) == 7
            and self.patente[0:2].isalpha()
            and self.patente[2:7].isdigit()
        ):
            return 1

        elif (
            len(self.patente) == 7
            and self.patente[0:3].isalpha()
            and self.patente[3].isdigit()
            and self.patente[4].isalpha()
            and self.patente[5:7].isdigit()
        ):
            return 2

        elif (
            len(self.patente) == 7
            and self.patente[0:4].isalpha()
            and self.patente[4:7].isdigit()
        ):
            return 3

        elif (
            len(self.patente) == 7
            and self.patente[0:3].isalpha()
            and self.patente[3:7].isdigit()
        ):
            return 4

        elif (
            len(self.patente) == 7
            and self.patente[0] == " "
            and self.patente[1:5].isalpha()
            and self.patente[5:7].isdigit()
        ):
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

    return (
        codigo_identificador,
        patente,
        tipo_de_vehiculo,
        forma_de_pago,
        pais_de_la_cabina,
        distancia,
    )


def menu():
    print("1) Crear arreglo de tickets desde un archivo")
    print("2) Cargar datos de un ticket por teclado")
    print(
        "3) Mostrar todos los registros del arreglo, ordenados por código de ticket, de menor a mayor"
    )
    print(
        "4) Buscar si existe en el arreglo un registro con una patente P y que haya pasado por un país X"
    )
    print(
        "5) Buscar si existe en el arreglo un registro con determinado código de ticket (SE DEBE CORRER LA OPCION 3 PREVIAMENTE PARA ORDENAR EL ARREGLO)"
    )
    print(
        "6) Determinar la cantidad de vehículos de cada país que pasaron por las cabinas"
    )
    print(
        "7) Determinar el importe acumulado por pagos de tickets, por cada uno de los posibles tipos de vehiculo"
    )
    print(
        "8) Mostrar cuál fue el tipo de vehículo con mayor monto acumulado, "
        "e indicar qué porcentaje representa ese monto sobre el total."
    )
    print(
        "9) Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos"
        " del arreglo, e informar cuántos de los vehículos recorrieron una distancia mayor a ese promedio"
    )
    print("0) Salir")
    opcion = int(input("Elija entre las siguientes opciones: "))
    return opcion


def cargar_tickets_desde_archivo(archivo):
    lines = abrir_archivo(archivo)

    conjunto_tickets = []  # El arreglo se crea de cero cada vez
    for line in lines:
        (
            identificador,
            patente,
            tipo_de_vehiculo,
            forma_de_pago,
            pais_de_la_cabina,
            distancia,
        ) = lectura_datos(line)

        nuevo_ticket = Ticket(
            identificador,
            patente,
            tipo_de_vehiculo,
            forma_de_pago,
            pais_de_la_cabina,
            distancia,
        )
        conjunto_tickets.append(nuevo_ticket)

    return conjunto_tickets


def cargar_ticket_por_teclado():
    identificador = validar_entre(
        0, 9999999999, "Introduzca el codigo de 10 dígitos del ticket: "
    )

    patente = input(
        "Introduzca la patente: "
    )  # No requiere validacion. Solo verifacion de pais de procedencia.
    if len(patente) == 6:
        patente = " " + patente  # Agrego un espacio en para mantener formato original

    tipo_de_vehiculo = validar_entre(
        0,
        2,
        "Introduzca el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ",
    )
    forma_de_pago = validar_entre(
        1, 2, "Introduzca forma de pago (1: manual, 2: telepeaje): "
    )
    pais_de_la_cabina = validar_entre(
        0,
        4,
        "Ingrese el país donde se cobró el peaje "
        "(0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ",
    )
    distancia = validar_entre(
        0,
        999,
        "Indique los kilómetros recorridos desde la cabina anterior (entre 0 y 999):",
    )
    nuevo_ticket = Ticket(
        identificador,
        patente,
        tipo_de_vehiculo,
        forma_de_pago,
        pais_de_la_cabina,
        distancia,
    )

    return nuevo_ticket


def validar_entre(lim_inferior, lim_superior, mensaje):
    n = lim_inferior - 1
    while n < lim_inferior or n > lim_superior:
        n = int(input(mensaje))
        if n < lim_inferior or n > lim_superior:
            print(f"ERROR! El número debe estar entre {lim_inferior} y {lim_superior}")
    return n


def ordenar(arreglo_tickets, descendente=False):
    n = len(arreglo_tickets)
    for i in range(n - 1):
        for j in range(i + 1, n):

            if (
                arreglo_tickets[j].identificador < arreglo_tickets[i].identificador
                and descendente == False
            ):
                arreglo_tickets[j], arreglo_tickets[i] = (
                    arreglo_tickets[i],
                    arreglo_tickets[j],
                )

            elif (
                arreglo_tickets[j].identificador > arreglo_tickets[i].identificador
                and descendente == True
            ):
                arreglo_tickets[j], arreglo_tickets[i] = (
                    arreglo_tickets[i],
                    arreglo_tickets[j],
                )


def mostrar_tickets_ordenados(arreglo_tickets):
    ordenar(arreglo_tickets)
    for ticket in arreglo_tickets:
        print(ticket)


# Actividad 4: Busqueda de patente que haya pasado por un pais determinado
def busqueda_patente(arreglo_tickets, p, x):
    """p: patente buscada. x: pais de la cabina"""
    n = len(arreglo_tickets)
    for i in range(n):
        if (
            arreglo_tickets[i].patente.lower() == p.lower()
            and arreglo_tickets[i].pais_cabina == x
        ):
            return i
    return -1


# Actividad 5: Busqueda de ticket
def busqueda_binaria_ticket(arreglo_tickets, c):
    """c: numero de ticket a buscar"""
    izq = 0
    der = len(arreglo_tickets)
    while izq <= der:
        posicion_analizada = (izq + der) // 2
        if arreglo_tickets[posicion_analizada].identificador == c:
            return posicion_analizada
        if arreglo_tickets[posicion_analizada].identificador > c:
            der = posicion_analizada - 1
        if arreglo_tickets[posicion_analizada].identificador < c:
            izq = posicion_analizada + 1
    return -1


# Actividad 6: Determinacion de cantidad de vehículos por pais
def cantidad_vehiculos(arreglo_tickets):
    n = len(arreglo_tickets)
    paises_posibles = 7
    vehiculos_por_pais = paises_posibles * [0]
    for i in range(n):
        vehiculos_por_pais[arreglo_tickets[i].numero_pais] += 1

    return vehiculos_por_pais


# Actividad 7: Calcular importe
def importe(arreglo_tickets):
    importe_final = 3 * [0]
    importe_base = 0

    for ticket in arreglo_tickets:

        # Se establece el importe BASE según país
        if (
            ticket.pais_cabina == 0
            or ticket.pais_cabina == 3
            or ticket.pais_cabina == 4
        ):
            importe_base = 300
        elif ticket.pais_cabina == 2:
            importe_base = 400
        elif ticket.pais_cabina == 1:
            importe_base = 200

        # Ajuste de importe BASE segun tipo de vehículo. Se obtiene el Importe BASICO
        if ticket.tipo_vehiculo == 0:
            importe_basico = 0.5 * importe_base
        elif ticket.tipo_vehiculo == 2:
            importe_basico = 1.6 * importe_base
        else:
            importe_basico = importe_base

        # Importe final del ticket, según forma de pago
        if ticket.forma_pago == 2:
            importe_final_del_ticket = importe_basico - (0.1 * importe_basico)
        else:
            importe_final_del_ticket = importe_basico

        c = ticket.tipo_vehiculo
        importe_final[c] += importe_final_del_ticket
    motocicleta = importe_final[0]
    automovil = importe_final[1]
    camion = importe_final[2]
    return motocicleta, automovil, camion


def imprimir_importe(arreglo_tickets):
    imprimir = importe(arreglo_tickets)

    print(
        "El el importe acumulado por pagos de tickets, por cada uno de los posibles tipos de vehiculo es: "
    )
    print(" Motocicleta: ", "$", imprimir[0])
    print(" Automóvil:   ", "$", imprimir[1])
    print(" Camión:      ", "$", imprimir[2])


# Actividad 8: Mayor monto
def mayor_monto(arreglo_tickets):
    a = importe(arreglo_tickets)
    if a[0] > a[1] and a[0] > a[2]:
        mayor_importe = a[0]
    elif a[1] > a[2]:
        mayor_importe = a[1]
    else:
        mayor_importe = a[2]
    print("El mayor importe es: $", mayor_importe)

    importe_total = a[0] + a[1] + a[2]
    porcentaje = (mayor_importe * 100) // importe_total

    print(
        "El porcentaje que representa el monto mayor sobre el monto total es de: ",
        porcentaje,
        "%",
    )


# Actividad 9: Distancia promedio
def distancia(arreglo_tickets):
    vehiculos, distancia_total_recorrida, mayor_al_promedio = 0, 0, 0
    for ticket in arreglo_tickets:

        distancia_total_recorrida += ticket.distancia
        vehiculos += 1
    distancia_promedio = distancia_total_recorrida // vehiculos
    print(
        "La distancia promedio desde la última cabina recorrida entre todos los vehículos es de: ",
        distancia_promedio,
        "km",
    )

    for ticket in arreglo_tickets:
        if ticket.distancia > distancia_promedio:
            mayor_al_promedio += 1
    print(
        "La cantidad de vehículos que recorrieron una distancia mayor que el promedio es: ",
        mayor_al_promedio,
    )
