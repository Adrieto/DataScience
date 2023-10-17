from alumno import *


def menu_opciones():
    print("1. Cargar alumnos.")
    print("2. Mostrar ordenados.")
    print("3. Cantidad de alumnos por nivel.")
    print("4. Obtener monto a pagar de un tutor por DNI.")
    print("5. Realizar descuento a alumno por DNI.")
    opcion = int(input("Ingrese su opcion: "))
    return opcion


def validar_mayor_que(limiteinf, mensaje):
    num = limiteinf
    while num <= limiteinf:
        num = int(input(mensaje))
        if num <= limiteinf:
            print("¡ERROR! No puede ser menor a ", limiteinf)
    return num


def validar_entre(inferior, superior, mensaje):
    numero = inferior - 1
    while numero <= inferior or numero >= superior:
        numero = int(input(mensaje))
        if numero <= inferior or numero >= superior:
            print('Error!!! El numero debe ser mayor o igual a', inferior, 'y menor igual a', superior)
    return numero


def carga_manual(vector,n):
    for i in range(n):
        print("Alumno ", i+1)
        dni = validar_entre(0,40000000, "DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni_tutor = validar_entre(0,40000000, "DNI tutor: ")
        importe = round(validar_mayor_que(0, "Importe: "), 2)
        nivel = validar_entre(1,10, "Nivel: ")
        alumno = Alumno(dni, nombre, apellido, dni_tutor, importe, nivel)
        vector.append(alumno)


def mostrar(vector):
    print(encabezado())
    for alumno in vector:
        print(alumno)


def ordenamiento(vector):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i].dni < vector[j].dni:
                vector[i], vector[j] = vector[j], vector[i]


def acumular_por_nivel(vector):
    v = [0] * 13
    for alumno in vector:
        v[alumno.nivel] += 1
    return v


def total_a_pagar(vector, x):
    total = 0
    for alumno in vector:
        if alumno.dni_tutor == x:
            total += alumno.importe
    return total


def buscar_alumno(vector, x):
    pos = -1
    for i in range(len(vector)):
        if vector[i].apellido == x:
            pos = i
            break
    return pos


def principal():
    op = -1
    alumnos = []

    while op != 0:
        op = menu_opciones()
        if op == 1:
            n = validar_mayor_que(0, "Ingrese cantidad de alumnos: ")
            carga_aleatoria(alumnos,n)
            """carga_manual(alumnos,n)"""
        if len(alumnos) > 0:
            if op == 2:
                ordenamiento(alumnos)
                mostrar(alumnos)
            elif op == 3:
                vc = acumular_por_nivel(alumnos)
                for i in range(len(vc)):
                    if vc[i] > 0:
                        print(f"El nivel {i} tiene un total de {vc[i]} alumnos.")
            elif op == 4:
                dni_tut = int(input("Ingrese el DNI del tutor: "))
                total = total_a_pagar(alumnos, dni_tut)
                print(f"El monto total a pagar es de: ${total:<10.2f}")
            elif op == 5:
                ape = input("Ingrese el apellido del alumno a buscar: ")
                pos = buscar_alumno(alumnos, ape)
                if pos != -1:
                    print("Alumno encontrado, descuento aplicado!!")
                    #alumnos[pos].importe *= 0.10
                    descuento = alumnos[pos].importe * 0.10
                    alumnos[pos].importe = descuento
                    print(encabezado())
                    print(alumnos[pos])
                else:
                    print("No existe el alumno.")
        else:
            print("Primero debe cargar alumnos.")


if __name__ == '__main__':
    principal()