import os.path
import pickle

import pacientes

NOMBRE_ARCHIVO = "pacientes.dat"

def menu():
    print("1 _ Cargar datos pacientes")
    print("2 _ Listar pacientes con mas de d dias")
    print("3 _ Buscar por historia clínica")
    print("4 _ Mostrar pacientes")
    print("5 _ Generar archivo pacientes")
    print("6 _ Mostrar archivo")
    print("7 _ ")
    print("8 _ ")
    print("9 _ Salir")
    return int(input("Ingrese opción: "))


def add_in_order_bad(v, paciente):
    pos = len(v)
    for i in range(len(v)):
        if v[i].nro_historia > paciente.nro_historia:
            pos = i
            break
    v[pos:pos] = [paciente]


def add_in_order(v, paciente):
    n = len(v)
    pos = -1
    izq = 0
    der = n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nro_historia == paciente.nro_historia:
            pos = c
            break
        elif v[c].nro_historia < paciente.nro_historia:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq

    v[pos:pos] = [paciente]


def cargar_pacientes(n):
    v = []
    for i in range(n):
        paciente = pacientes.cargar_paciente_random()
        add_in_order(v, paciente)
    return v


def mostrar(v):
    for paciente in v:
        print(paciente)


def validar_mayor(minimo, mensaje):
    num = int(input(mensaje))
    while num < minimo:
        print("Error. Debe ingresar un valor mayor a", minimo)
        num = int(input("Ingrese valor: "))
    return num


def mostrar_mas_dias(v, d):
    for paciente in v:
        if paciente.dias > d:
            print(paciente)


def buscar_por_historia(v, x):
    izq = 0
    der = len(v) - 1
    res = None
    # Mientras no se crucen
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nro_historia == x:
            # Lo encontré
            res = v[c]
            break
        elif v[c].nro_historia < x:
            # Es mas grande que el central, busco en la parte derecha
            izq = c + 1
        else:
            # Es mas chico que el central, busco en la parte izquierda
            der = c - 1
    return res


def generar_archivo(v):
    archivo = open(NOMBRE_ARCHIVO, "wb")

    for paciente in v:
        pickle.dump(paciente, archivo)

    archivo.close()


def mostrar_archivo():
    if os.path.exists(NOMBRE_ARCHIVO):
        archivo = open(NOMBRE_ARCHIVO, "rb")

        tam = os.path.getsize(NOMBRE_ARCHIVO)
        # Mientras no llegue al final
        while archivo.tell() < tam:
            paciente = pickle.load(archivo)
            print(paciente)

        archivo.close()
    else:
        print("El archivo no existe")


def generar_arreglo_desde_archivo():
    v = []
    if os.path.exists(NOMBRE_ARCHIVO):
        archivo = open(NOMBRE_ARCHIVO, "rb")

        tam = os.path.getsize(NOMBRE_ARCHIVO)
        # Mientras no llegue al final
        while archivo.tell() < tam:
            paciente = pickle.load(archivo)
            if paciente.cod_enfermedad in (8, 9):
                v.append(paciente)

        archivo.close()
        return v
    else:
        print("El archivo no existe")

def principal():
    op = -1
    v = []
    v2 = None
    while op != 9:
        op = menu()

        if op == 1:
            n = int(input("Ingrese cantidad a cargar: "))
            v = cargar_pacientes(n)
            mostrar(v)
        elif op == 6:
            mostrar_archivo()
        elif op == 7:
            v2 = generar_arreglo_desde_archivo()
        elif op == 8:
            if v2 is None:
                print("Debe generar el arreglo del punto 7 primero")
            else:
                mostrar(v2)
        elif len(v) == 0:
            print("Debe cargar el arreglo primero")
        elif op == 2:
            d = validar_mayor(0, "Ingrese cantidad de dias: ")
            mostrar_mas_dias(v, d)
        elif op == 3:
            x = validar_mayor(0, "Ingrese número de historia clínica: ")
            res = buscar_por_historia(v, x)
            if res is None:
                print("No se encontró")
            else:
                print("Se encontró. Sus datos son")
                print(res)
        elif op == 4:
            mostrar(v)
        elif op == 5:
            generar_archivo(v)


if __name__ == '__main__':
    principal()
