# TP4 Patentes y peajes

from ticket import Ticket
from funciones_varias import *


def main():
    nombre_csv = "peajes-tp4.csv"
    nombre_binario = "peajes.dat"
    bandera_crear_de_cero = True
    opcion = -1


    while opcion != 0:
        opcion = menu()

        # OPCION 1: CARGA DE TICKETS POR MEDIO DE .CSV Y GUARDADO A BINARIO
        if opcion == 1:
            modo_escritura = "wb"

            if bandera_crear_de_cero:
                datos = abrir_archivo(nombre_csv)
                save_binary(datos, nombre_binario, modo_escritura)
                bandera_crear_de_cero = False  # Ya se creó el archivo
            else:
                borrar = input("Si continúa, se sobrescribirá el archivo binario. Desea continuar (S/N): ")
                if borrar in "sS":
                    datos = abrir_archivo(nombre_csv)
                    save_binary(datos, nombre_binario, modo_escritura)
                    print("\t El archivo fue sobre escrito con éxito.\n")
                else:
                    continue

        # OPCION 2: CARGA DE TICKET POR TECLADO Y GUARDADO.
        elif opcion == 2:
            ticket_teclado = cargar_ticket_por_teclado()
            if bandera_crear_de_cero:
                modo_escritura = "wb"
                bandera_crear_de_cero = False
            elif not bandera_crear_de_cero:
                modo_escritura = "ab"
            guardar_ticket_a_binario(ticket_teclado, nombre_binario, modo_escritura)

        elif bandera_crear_de_cero:
                print("\tTodavia no hay tickets cargados. Utilice las opciones 1 o 2 para cargar tickets\n")

        # OPCION 3: MUESTRA TICKETS DEL ARREGLO, ORDENADOS DE MENOR A MAYOR POR CÓDIGO DE TICKET
        elif opcion == 3:
            if bandera_crear_de_cero:
                print("\tTodavia no hay tickets cargados. Por favor, cargue datos con las opciones 1 o 2.\n")
            else:
                leer_datos_desde_binario(nombre_binario)

        # OPCION 4: BUSQUEDA DE UNA PATENTE DESDE ARCHIVO BINARIO
        elif opcion == 4:
            patente_a_buscar = str(input('Ingresa la patente a buscar: '))
            patente_encontrada = buscar_por_patente(nombre_binario, patente_a_buscar)
            if len(patente_encontrada) > 0:
                print(f'{len(patente_encontrada)} Patente/s encontrada/s. Sus datos son:')
                for ticket in patente_encontrada:
                    print(ticket)
            else:
                print('\tLa patente solicitada no se encuentra registrada. \n')

        # OPCION 5: BUSCAR UN ARREGLO SEGUN IDENTIFICADOR DE TICKET
        elif opcion == 5:
            c = validar_mayor(0, "Ingrese el numero de ticket a buscar (mayor a 0): ")
            ticket_buscado = buscar_por_identificador(nombre_binario, c)
            if ticket_buscado != -1:
                print(f"\tSe encontró el ticket numero {c}. Sus datos son:")
                print(f"\t {ticket_buscado}")
            else:
                print(f"\tNo se encontró el ticket numero {c}")

        # OPCION 6: COMBINACIONES DE CANTIDAD DE VEHICULOS POR TIPO Y POR PAIS DE LA CABINA
        elif opcion == 6:
            combinaciones = cantidad_por_tipo_y_pais(nombre_binario)
            print("Cantidad de vehículos por pais y tipo de vehículo".upper())
            for i in range(len(combinaciones)):
                print(f"{VEHICULOS[i].upper()}:")
                for j in range(len(combinaciones[i])):
                    if combinaciones[i][j] > 0:
                        print(f"\t{PAISES[j]}: {combinaciones[i][j]}")
                print()

        # OPCION 7: CANTIDADES TOTAL DE VEHICULOS POR TIPO Y POR PAIS DE CABINA
        elif opcion == 7:
            matriz_comb = cantidad_por_tipo_y_pais(nombre_binario)
            print("Cantidad total de vehículos, según su tipo: ")
            por_tipo(matriz_comb)
            print("Cantidad total de vehículos, según país de la cabina: ")
            por_pais(matriz_comb)

        # OPCION 8: DISTANCIA PROMEDIO
        elif opcion == 8:
            print("\t\tCalculando...")
            tickets_mayores_promedio = []
            promedio = promedio_distancias(nombre_binario)
            generar_arreglo(nombre_binario, tickets_mayores_promedio, promedio)
            shellsort(tickets_mayores_promedio)

            for ticket in tickets_mayores_promedio:
                print(ticket)

            print(f"\n\tEl promedio de las distancias recorridas es: {promedio} km\n")

        # OPCION 0: TERMINAR
        elif opcion == 0:
            print("Proceso terminado. ¡Gracias por utilizar nuestros servicios!")
            break


if __name__ == "__main__":
    main()
