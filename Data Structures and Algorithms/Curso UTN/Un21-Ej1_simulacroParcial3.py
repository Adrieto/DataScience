# (Parcial 2019) - Servicios de Limpieza
# Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos.
# Por cada trabajo se tienen los siguientes datos: el número de identificación del trabajo,
# la descripción o nombre del mismo, el tipo de trabajo (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados),
# el importe a cobrar por ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar
# la información referida a los n trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
# 1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo
# sea positivo y que el importe a cobrar sea mayor a cero. Puede hacer la carga en forma manual, o puede generar
# los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero
# al menos una debe programar.
# 2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.
# 3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay
# varios trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal
# sea máxima).
# 4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado.
# Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida
# con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
# 5- Determinar y mostrar la cantidad de trabajos por tipo.

import random

class Trabajo():
    def __init__(self, identificacion, descripcion, tipo_trabajo, importe, personal_afectado):
        self.identificacion = identificacion
        self.descripcion = descripcion
        self.tipo_trabajo = tipo_trabajo
        self.importe = importe
        self.personal_afectado = personal_afectado

    def __str__(self):
        return f"Identificacion: {self.identificacion}, descripcion: {self.descripcion}, tipo de trabajo: " \
               f"{self.tipo_trabajo}, Importe: ${self.importe}, personal afectado: {self.personal_afectado} personas"


def menu():
    print("Menú de opciones:")
    print("1) Cargar arreglo")
    print("2) Mostrar todos los datos de todos los trabajos, segun importe")
    print("3) Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado")
    print("4) Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado.")
    print("5) Determinar y mostrar la cantidad de trabajos por tipo.")
    print("0) Salir")
    opcion = int(input("Elija una opcion: "))
    return opcion


# Punto 1
def cargar_registros(n):
    DESCRIPCIONES = ("Limpieza", "Desinfeccion", "Desengrasado", "Esterilizacion")

    arreglo_trabajos = []
    for i in range(n):
        identificacion = i
        while identificacion < 0:
            identificacion = random.choice((-i, i)) #Simula una validacion
        descripcion = random.choice(DESCRIPCIONES)
        tipo_trabajo = random.randint(0,3)
        importe = random.randint(-8500, 8500)
        while importe <= 0:
            importe = random.randint(-8500, 8500)
        personal_afectado = random.randint(1, 10)
        nuevo_trabajo = Trabajo(identificacion, descripcion, tipo_trabajo, importe, personal_afectado)
        arreglo_trabajos.append(nuevo_trabajo)
    return arreglo_trabajos

# Punto 2:
def ordenar_registro_por_importe(arreglo_trabajos):
    n = len (arreglo_trabajos)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo_trabajos[i].importe < arreglo_trabajos[j].importe:
                arreglo_trabajos[i], arreglo_trabajos[j] = arreglo_trabajos[j], arreglo_trabajos[i]

# 3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado

def trabajo_maximo_personal(registros_trabajo):
    maximo = 0
    posicion_maximo = -1
    n = len(registros_trabajo)
    for i in range(n):
        if registros_trabajo[i].personal_afectado > maximo:
            maximo = registros_trabajo[i].personal_afectado
            posicion_maximo = i
    return maximo, posicion_maximo


def main():
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            # 1- Cargar el arreglo pedido con los datos de los n trabajos.
            n = int(input("Ingrese cantidad de registros a generar: "))
            registros_trabajo = cargar_registros(n)

        if opcion == 2:
        # 2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.
            ordenar_registro_por_importe(registros_trabajo)

            # Mostrar registros ordenados:
            for i in range(n):
                print(registros_trabajo[i])

        if opcion == 3:
            # 3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado
            maximo_personal, posicion = trabajo_maximo_personal(registros_trabajo)
            print(f"\nEl trabajo con identificacion {registros_trabajo[posicion].personal_afectado}"
                  f" es el que tiene mas personal asignado: {maximo_personal} personas.\n")





if __name__ == '__main__':
    main()