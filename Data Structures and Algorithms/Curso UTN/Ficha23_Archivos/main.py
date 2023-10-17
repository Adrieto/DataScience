# 6. Club Deportivo
# Un club deportivo necesita procesar los pagos realizados por sus socios. Para ello, se cuenta con un archivo
# denominado cuotas.dat, donde cada registro contiene:
#
#   - Número de socio.
#   - Deporte que realiza (0: Natacion/1: Basquet/2: Karate/3: Futbol/ 4: Patin).
#   - Día del mes en que pagó.
#   - Valor de la cuota.
#   - Si el socio aún no abonó, el día del mes debe ser 0.
#
# Se debe cargar el archivo en un vector y luego implementar un menú con las siguientes opciones:
#
#   1. Consulta: mostrar el contenido del vector.
#   2. Cobro: buscar un socio y deporte ingresados por teclado. Si el registro existe, registrar el día y valor de
#   pago (también    ingresado por teclado). Si no, agregar un nuevo registro en el vector con esos datos. Informar
#   el cambio realizado.
#   3. Morosos: generar un archivo de texto conteniendo los registros de los socios que aun no pagaron la cuota.
#   4. Totales: indicar cantidad de cobros por cada deporte, y cuál es el deporte con mayor cantidad de participantes.
#   5. Grabar: reemplazar el archivo pagos.dat con el contenido del vector. Mostrar el contenido del archivo.

import os.path
import pickle
from registro import *


def menu():
    print("Menú de opciones")
    print("1) Consulta: mostrar el contenido del vector")
    print("2) Cobro: buscar un socio y deporte ingresados por teclado")
    print("3) Morosos: genera archivo txt con datos de morosos")
    print("4) cantidad de cobros por cada deporte, y cuál es el deporte con mayor cantidad de participantes")
    print("5) Grabar: reemplazar el archivo pagos.dat con el contenido del vector.")
    print("0) Salir")
    opcion = int(input("Elija una opción: "))
    return opcion


def leer_archivo(nombre):
    lista = []
    tamaño = os.path.getsize(nombre)
    archivo = open(nombre, "rb")
    while archivo.tell() < tamaño:
        obj = pickle.load(archivo)
        lista.append(obj)
    archivo.close()
    return lista


def imprimir_archivo(nombre):
    archivo = open(nombre, "rb")
    tamaño = os.path.getsize(nombre)
    while archivo.tell() < tamaño:
        print(pickle.load(archivo))


def grabar_archivo(lista, nombre):
    archivo = open(nombre, "wb")
    for c in lista:
        pickle.dump(c, archivo)
    archivo.close()


def grabar_archivo_texto(lista, nombre_archivo):
    archivo = open(nombre_archivo, "wt")
    for cuota in lista:
        archivo.write(f"{cuota.__str__()}  \n")


#   2. Cobro: buscar un socio y deporte ingresados por teclado. Si el registro existe, registrar el día y valor de
#   pago (también    ingresado por teclado). Si no, agregar un nuevo registro en el vector con esos datos. Informar
#   el cambio realizado.
def buscar_registro(listado, socio, deporte):
    for i in range(len(listado)):
        if listado[i].socio == socio and listado[i].deporte == deporte:
            return i


def mostrar_vector(v):
    for objeto in v:
        print(objeto)


def buscar_morosos(listado):
    morosos = []
    for cuota in listado:
        if cuota.dia == 0:
            morosos.append(cuota)
    return morosos


#   4. Totales: indicar cantidad de cobros por cada deporte, y cuál es el deporte con mayor cantidad de participantes.
def cobros_por_deporte(vector):
    cobros = 6 * [0]
    for cuota in vector:
        cobros[cuota.deporte] += cuota.valor_cuota
    return cobros


def participantes_deporte(vector):
    cant_participantes = 6 * [0]
    for cuota in vector:
        cant_participantes[cuota.deporte] += 1
    return cant_participantes


def principal():
    opcion = -1
    nombre = "cuotas.dat"
    listado = leer_archivo(nombre)

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            mostrar_vector(listado)

        #   2. Cobro: buscar un socio y deporte ingresados por teclado. Si el registro existe, registrar el día y valor de
        #   pago (también ingresado por teclado). Si no, agregar un nuevo registro en el vector con esos datos. Informar
        #   el cambio realizado.
        elif opcion == 2:
            socio_buscado = int(input("Ingrese numero de socio: "))
            deporte_buscado = int(input("Ingrese deporte: "))
            buscado = buscar_registro(listado, socio_buscado, deporte_buscado)
            if buscado:
                print(f"Elemento buscado({buscado}):\n {listado[buscado]}")
                listado[buscado].dia = int(input("ingrese dia de pago: "))
                listado[buscado].valor_cuota = float(input("ingrese valor de la cuota: "))
                print(f"Elemento modificado:\n {listado[buscado]}")
            else:
                print("El socio y deporte no existen. Ingrese por teclado los siguientes datos")
                dia = int(input("Dia de pago de la cuota (0 si todavia no pagó): "))
                valor_cuota = int(input("Monto de la cuota que debe pagar el socio: "))
                nueva_cuota = Cuota(socio_buscado, deporte_buscado, dia, valor_cuota)
                listado.append(nueva_cuota)

        #   3. Morosos: generar un archivo de texto conteniendo los registros de los socios que aun no pagaron la cuota.
        elif opcion == 3:
            nombre_archivo = "morosos.txt"
            morosos = buscar_morosos(listado)
            grabar_archivo_texto(morosos, nombre_archivo)

        #   4. Totales: indicar cantidad de cobros por cada deporte, y cuál es el deporte con mayor cantidad de participantes.
        elif opcion == 4:
            monto_total_deporte = cobros_por_deporte(listado)
            for i in range(len(monto_total_deporte)):
                print(f"Monto total deporte{[i]}: ${round(monto_total_deporte[i],2)}")

            participantes = participantes_deporte(listado)
            print(f"Cantidad de participantes por deporte: {participantes}")


        #   5. Grabar: reemplazar el archivo pagos.dat con el contenido del vector. Mostrar el contenido del archivo.
        elif opcion == 5:
            nombre = "cuotas2.dat"
            grabar_archivo(participantes, nombre)
            print(f"Imprimo contenido del archivo'{nombre}'")
            imprimir_archivo(nombre)



if __name__ == '__main__':
    principal()
