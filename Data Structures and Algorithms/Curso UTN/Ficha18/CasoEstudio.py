# Con los datos de n notas de los alumnos obtenidas en el primer parcial de un
# curso, se pide:
# 1. Cargar en un vector las notas (generarlas en forma automática).
# 2. Mostrar sus datos.
# 3. Mostrar el promedio de notas del curso.
# 4. Mostrar las notas mayor a 8.
# 5. Generar y mostrar un vector de 10 contadores, donde cada posición
# representa la escala de notas del 1 al 10 y los valores del vector
# representan las cantidades de alumnos que tuvieron la nota según la escala
# de notas.
# 6. Mostrar las notas ordenadas de menor a mayor por nota.
# 7. Buscar una nota ingresada por teclado si se encuentra, indicar cuantos
# alumnos tuvieron esa nota, sino informar que no se encuentra.


import random

# Funciones -- BackEnd
# 1. Cargar en un vector las notas (generarlas en forma automática).
def cargar_vector(vec, n):
    for i in range (n):
        nota = random.randint(1,10)
        vec.append(nota)

# 2. Mostrar sus datos.
def mostrar_vector(vec):
    largo = len(vec)
    cadena = ""
    for i in range (largo):
        cadena += str(vec[i]) + ", "
    cadena = cadena[:-2] # Para eliminar la ultima coma
    print(cadena)

# 3. Mostrar el promedio de notas del curso.
def promedio_notas(vec):
    ac_notas = 0
    promedio = None
    cantidad = len(vec)

    if cantidad > 0:
        for nota in vec:
            ac_notas += nota
        promedio = ac_notas / cantidad
    return promedio

# 4. Mostrar las notas mayor a 8.
def notas_mayor8(vec):
    for nota in vec:
        if nota > 8:
            print(nota, end=",")

# 5. Generar y mostrar un vector de 10 contadores que representa la escala de notas del 1 al 10 y los
# valores del vector representan las cantidades de alumnos que tuvieron la nota según la escala de notas.
def contadores_notas(vec):
    contadores = 10 * [0]

    for nota in vec:
        j = nota - 1
        contadores[j] += 1

    return contadores

# 6. Mostrar las notas ordenadas de menor a mayor por nota.
def ordenar_notas(vec):
    n = len (vec)
    for i in range (n-1):
        for j in range(i+1, n):
            if vec[j] <= vec[i]:
                vec[i], vec[j] = vec[j], vec[i]

# 7. Buscar una nota ingresada por teclado si se encuentra, indicar cuantos
# alumnos tuvieron esa nota, sino informar que no se encuentra.
def busqueda(vec, buscado):
    cont_buscado = 0
    se_encontro = False
    for nota in vec:
        if nota == buscado:
            cont_buscado += 1
            se_encontro = True
    return se_encontro, cont_buscado



def main():  #FrontEnd
    vec = []
    n = input("ingrese numero de elementos a cargar en el vector: ")
    while True:
        if n.isdigit() and int(n)>0:
            n = int(n)
            break
        n = input("Incorrecto. Ingrese un numero mayor que cero: ")

    cargar_vector(vec, n)
    mostrar_vector(vec)
    promedio = promedio_notas(vec)
    print(f"El promedio de las notae es: {promedio} \n")
    print("Listado de notas mayores a 8: ")
    notas_mayor8(vec)

    print("Punto 5. CONTADORES DE NOTAS:")
    cantidad_cada_nota = contadores_notas(vec)
    for idx, contador in enumerate(cantidad_cada_nota):
        print(f"Cantidad de '{idx+1}': {contador}")
    print("\n Notas ordenadas de menor a mayor: ")
    ordenar_notas(vec)
    mostrar_vector(vec)

    # Busqueda de valores en la lista de notas y conteo de apariciones
    valor_buscado = input("Introduzca valor a buscar: ")
    if valor_buscado.isdigit():
        valor_buscado = int(valor_buscado)

    existe, nro_apariciones = busqueda(vec, valor_buscado)
    if existe:
        print (f"El valor '{valor_buscado}' apareció {nro_apariciones} veces.")
    else:
        print(f"No se encontró el valor '{valor_buscado}' entre las notas")


if __name__ == '__main__':
    main()