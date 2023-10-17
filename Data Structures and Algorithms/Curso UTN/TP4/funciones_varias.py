import pickle
import os.path
from ticket import *
import io

PAISES = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros")
VEHICULOS = ("motocicletas", "automóviles", "camiones")

def menu():
    print("--------MENÚ DE OPCIONES--------")
    print("1) Crear archivo binario de registros de tickets.")
    print("2) Cargar datos de un ticket por teclado al archivo binario.")
    print("3) Mostrar los datos de todos los registros del archivo binario.")
    print("4) Mostrar todos los registros del archivo binario cuya patente sea igual a p, un valor pasado por teclado.")
    print("5) Buscar en el archivo binario un ticket cuyo código sea igual a c, un valor pasado por teclado.")
    print("6) Determinar y mostrar la cantidad de vehículos de cada combinación posible entre tipo de vehículo"
          " y país de cabina en el archivo binario.")
    print("7) Mostrar la cantidad total de vehículos contados por cada tipo de vehículo posible, y la cantidad total"
          " de vehículos contados por cada país de cabina posible.")
    print("8) Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del archivo binario.")
    print("0) Salir.")
    opcion = int(input("Elija entre las siguientes opciones: "))
    return opcion


def abrir_archivo(nombre_archivo):
    """Abre archivo .csv y elimina su timestamp"""
    archivo = open(nombre_archivo)
    lines = archivo.readlines()
    archivo.close()
    lines = lines[2:]  # timestamp y nombres de columnas eliminados
    return lines


def save_binary(datos, nombre_archivo, modo):
    archivo_binario = open(nombre_archivo, modo)
    for linea in datos:
        identificador, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia = linea.strip().split(",")
        nuevo_ticket = Ticket(identificador, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia)
        pickle.dump(nuevo_ticket, archivo_binario)
    archivo_binario.close()


def guardar_ticket_a_binario(ticket, nombre_archivo, modo):
    archivo_binario = open(nombre_archivo, modo)
    pickle.dump(ticket, archivo_binario)
    archivo_binario.close()


def leer_datos_desde_binario(nombre_archivo):
    tamaño = os.path.getsize(nombre_archivo)
    archivo = open(nombre_archivo, "rb")
    while archivo.tell() < tamaño:
        ticket = pickle.load(archivo)
        print(ticket)
    archivo.close()


def promedio_distancias(nombre_archivo):
    archivo = open(nombre_archivo, "rb")
    tamaño = os.path.getsize(nombre_archivo)
    acum = cont = 0
    while archivo.tell() < tamaño:
        ticket = pickle.load(archivo)
        acum += ticket.distancia
        cont += 1
    archivo.close()
    promedio = round(acum / cont, 2)
    return promedio


def generar_arreglo(nombre_archivo, tickets_mayores_promedio, promedio):
    archivo = open(nombre_archivo, "rb")
    tamaño = os.path.getsize(nombre_archivo)
    while archivo.tell() < tamaño:
        ticket = pickle.load(archivo)
        if ticket.distancia > promedio:
            tickets_mayores_promedio.append(ticket)


def shellsort(vector):
    n = len(vector)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y_distancia = vector[j].distancia
            y_objeto = vector[j]
            k = j - h
            while k >= 0 and vector[k].distancia > y_distancia:
                vector[k+h] = vector[k]
                k -= h
            vector[k+h] = y_objeto
        h //= 3


def buscar_por_patente (nombre_archivo, patente_a_buscar):
    m = open(nombre_archivo, 'rb')
    tickets_encontrados = []
    t = os.path.getsize(nombre_archivo)
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)
    while m.tell() < t:
        fp = m.tell()
        ticket = pickle.load(m)
        if ticket.patente == patente_a_buscar:
            tickets_encontrados.append(ticket)
    m.seek(fp_inicial, io.SEEK_SET)
    return tickets_encontrados


def buscar_por_identificador (nombre_archivo, patente_a_buscar):
    m = open(nombre_archivo, 'rb')
    t = os.path.getsize(nombre_archivo)
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)
    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        ticket = pickle.load(m)
        if ticket.identificador == patente_a_buscar:
            return ticket
    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


def cantidad_por_tipo_y_pais(nombre_archivo):
    if os.path.exists(nombre_archivo):
        matriz_comb = [[0] * 5, [0] * 5, [0] * 5]
        t = os.path.getsize(nombre_archivo)
        archivo = open(nombre_archivo, 'rb')
        while archivo.tell() < t:
            comb = pickle.load(archivo)
            vehiculo = int(comb.tipo_vehiculo)
            pais = int(comb.pais_cabina)
            matriz_comb[vehiculo][pais] += 1
        archivo.close()
    return matriz_comb


def por_tipo(matriz):
    i = len(matriz)
    j = len(matriz[0])
    vehiculo = -1
    for f in range(i):
        cont = 0
        vehiculo += 1
        for c in range(j):
            cont += matriz[f][c]
        print(f"\t{VEHICULOS[vehiculo]}:  {cont}")


def por_pais(matriz):
    i = len(matriz)
    j = len(matriz[0])
    pais = -1
    for c in range(j):
        cont = 0
        pais += 1
        for f in range(i):
            cont += matriz[f][c]
        print(f"\t{PAISES[pais]}: {cont}")




