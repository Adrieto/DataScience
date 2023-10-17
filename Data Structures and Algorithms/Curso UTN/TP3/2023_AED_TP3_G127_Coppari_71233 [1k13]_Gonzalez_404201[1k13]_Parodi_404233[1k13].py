from ticket import *

# TP3 Patentes y peajes
# Formatos posibles:
PAISES = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros")
# Argentina: LLNNNLL     "AK348LZ"
# Bolivia:   LLNNNNN     "AP85986"
# Brasil:    LLLNLNN     "ASF5Q99"
# Paraguay:  LLLLNNN     "ASFQ849"
# Uruguay:   LLLNNNN     "ASF8492"
# Chile:      LLLLNN     " LANY87"
# Otro:      Cualquier otro formato


def main():
    bandera_crear_arreglo = True
    opcion = -1
    # Menú de opciones:
    while opcion != 0:
        opcion = menu()

        # OPCION 1: CARGA DE TICKETS A TRAVES DE CARGA DE ARCHIVO
        if opcion == 1:
            if bandera_crear_arreglo:
                arreglo_tickets = []
                bandera_crear_arreglo = False  # Ya se creó el arreglo
            else:
                borrar = input(
                    "Está a punto de borrar el arreglo cargado previamente. Desea continuar (S/N): "
                )
                if borrar in "sS":
                    arreglo_tickets = []
                else:
                    continue
            archivo = "peajes-tp3.txt"
            arreglo_tickets = cargar_tickets_desde_archivo(archivo)

        # OPCION 2: CARGA DE TICKETS POR TECLADO.
        elif opcion == 2:
            if bandera_crear_arreglo:
                arreglo_tickets = []
                bandera_crear_arreglo = False
            ticket_por_teclado = cargar_ticket_por_teclado()
            arreglo_tickets.append(ticket_por_teclado)

        # OPCION 3: MUESTRA TICKETS DEL ARREGLO, ORDENADOS DE MENOR A MAYOR POR CÓDIGO DE TICKET
        elif opcion == 3:
            if bandera_crear_arreglo:
                print("Todavia no hay tickets cargados. Pruebe otra opción")
            else:
                mostrar_tickets_ordenados(arreglo_tickets)

        # OPCION 4: BUSQUEDA DE UNA PATENTE
        elif opcion == 4:
            p = input("Ingrese la patente a buscar: ")
            x = validar_entre(
                0, 4, "Ingrese el pais de la cabina deseado (entre 0 y 4): "
            )
            posicion_patente = busqueda_patente(arreglo_tickets, p, x)
            if posicion_patente != -1:
                print("Se encontró la patente. Sus datos son:")
                print(arreglo_tickets[posicion_patente])
            else:
                print(
                    f"La patente buscada {p} no pasó por el pais '{x}' o no existe en el arreglo"
                )

        # OPCION 5: BUSCAR UN ARREGLO SEGUN CODIGO DE TICKET
        elif opcion == 5:
            c = validar_entre(0, 9999999999, "Ingrese el numero de ticket a buscar: ")
            posicion_ticket_buscado = busqueda_binaria_ticket(arreglo_tickets, c)
            if posicion_ticket_buscado != -1:
                forma_de_pago = arreglo_tickets[posicion_ticket_buscado].forma_pago
                arreglo_tickets[posicion_ticket_buscado].forma_pago = (
                    1 if forma_de_pago == 2 else 1
                )
                print("Ticket con medio de pago modificado: ")
                print(arreglo_tickets[posicion_ticket_buscado])
            else:
                print(f"No se encontró el ticket numero {c}")

        # OPCION 6: CANTIDAD DE VEHICULOS DE CADA PAIS QUE PASARON POR LAS CABINAS
        elif opcion == 6:
            vehiculos_por_pais = cantidad_vehiculos(arreglo_tickets)
            for i in range(len(vehiculos_por_pais)):
                print(f"Vehículos de '{PAISES[i]}': {vehiculos_por_pais[i]}")

        # OPCION 7: CALCULAR IMPORTE ACUMULADO
        elif opcion == 7:
            if bandera_crear_arreglo:
                print("Todavia no hay tickets cargados. Pruebe otra opción")
            else:
                imprimir_importe(arreglo_tickets)

        # OPCION 8: TIPO DE VEHICULO CON MAYOR MONTO ACUMULADO
        elif opcion == 8:
            if bandera_crear_arreglo:
                print("Todavia no hay tickets cargados. Pruebe otra opción")
            else:
                mayor_monto(arreglo_tickets)

        # OPCION 9: DISTANCIA PROMEDIO
        elif opcion == 9:
            if bandera_crear_arreglo:
                print("Todavia no hay tickets cargados. Pruebe otra opción")
            else:
                distancia(arreglo_tickets)

        # OPCION 0: TERMINAR
        elif opcion == 0:
            print("Proceso terminado. ¡Gracias por utilizar nuestros servicios!")
            break

        auxiliar = input("\nPresione enter para repetir el menú de opciones")


if __name__ == "__main__":
    main()
