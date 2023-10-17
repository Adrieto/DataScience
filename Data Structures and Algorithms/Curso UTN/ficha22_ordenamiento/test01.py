import time
import ordenamiento

__author__ = 'Cátedra de AED'


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def test():
    op = 0
    arreglo_creado = False
    while op != 9:
        print('1. Generar el vector')
        print('2. Verificar orden')
        print('3. Ordenamiento por Selección Directa')
        print('4. Ordenamiento por Intercambio Directo (Burbuja)')
        print('5. Ordenamiento por Inserción Directa')
        print('6. Ordenamiento Heapsort')
        print('7. Ordenamiento Quicksort')
        print('8. Ordenamiento Shellsort')
        print('9. Salir')

        op = int(input('\t\tIngrese opción: '))
        while not arreglo_creado and 1 < op < 9:
            print("El arreglo todavía no ha sido creado, carguelo con la opcion 1.")
            op = int(input('\t\tIngrese 1 para cargar arreglo, o 9 para salir: '))

        if op == 1:
            print()
            n = validate(0)
            v = n * [0]
            ordenamiento.generate_random(v)
            print('Hecho... arreglo creado...')
            print()
            arreglo_creado = True

        elif op == 2:
            print()
            if ordenamiento.check(v):
                print('Está ordenado...')
            else:
                print('No está ordenado...')
            print()

        elif op == 3:
            print()
            print('Ordenamiento: Selección Directa.')
            t1 = time.perf_counter()
            ordenamiento.selection_sort(v)
            t2 = time.perf_counter()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 4:
            print()
            print('Ordenamiento: Intercambio Directo (Burbuja).')
            t1 = time.perf_counter()
            ordenamiento.bubble_sort(v)
            t2 = time.perf_counter()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 5:
            print()
            print('Ordenamiento: Inserción Directa.')
            t1 = time.perf_counter()
            ordenamiento.insertion_sort(v)
            t2 = time.perf_counter()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 6:
            print()
            print('Ordenamiento: Heap Sort.')
            t1 = time.perf_counter()
            ordenamiento.heap_sort(v)
            t2 = time.perf_counter()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 7:
            print()
            print('Ordenamiento: Quick Sort.')
            t1 = time.perf_counter()
            ordenamiento.quick_sort(v)
            t2 = time.perf_counter()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()

        elif op == 8:
            print()
            print('Ordenamiento: Shell Sort.')
            t1 = time.perf_counter()
            ordenamiento.shell_sort(v)
            t2 = time.perf_counter()
            tt = t2 - t1
            print('Hecho... Tiempo total insumido:', tt, 'segundos')
            print()


# script principal...
if __name__ == '__main__':
    test()
