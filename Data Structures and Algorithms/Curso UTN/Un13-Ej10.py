"""Procesar el archivo de texto con datos de los alumnos que puede descargar haciendo click aquí,
cada fila de datos contiene los datos de los alumnos en un esquema de cantidad fija de caracteres.
De cada alumno figura, el legajo, nombre, nota del parcial 1, nota del parcial 2, nota del parcial 3
 y nota de trabajos prácticos

Se necesita procesar el archivo para conocer la cantidad de alumnos por cada estado académico:
* Cantidad de alumnos Libres
* Cantidad de alumnos Regulares
* Cantidad de alumnos aprobados

Para aprobar el alumno debe tener en los parciales promedio de 8 con nota no menor a 7 y en la nota de tps 8 o más,
 para regularizar debe tener 2 de los 3 parciales aprobados con nota 4 o más y los trabajos prácticos con nota 4
 o más y en caso contrario está libre.

También es necesario mostrar un listado con los alumnos aprobados agregando a cada alumno su nota final que surge
 promedio directo de las 4 notas del alumno.

Finalmente, el programa debe mostrar el porcentaje de cada condición de alumno respecto del total del curso. """


def test():
    archivo = open("Notas Alumnos.txt")
    texto = archivo.readlines()
    archivo.close()

# Contadores
    cant_aprobados = cant_regulares = cant_libres = contador_total = 0
    listado_aprobado = ""

    for line in texto:
        palabras = line.split()
        #print(palabras)
        nota_tp = int(palabras[-1])
        nota_par3 = int(palabras[-2])
        nota_par2 = int(palabras[-3])
        nota_par1 = int(palabras[-4])
        prom_parciales = (nota_par1 + nota_par2 + nota_par3) / 3
        promedio_final = (nota_par1 + nota_par2 + nota_par3 + nota_tp) / 4

        contador_total += 1

        if prom_parciales >= 8 and nota_par1 >= 7 and nota_par2 >= 7 and nota_par3 >= 7 and nota_tp >= 8:
            cant_aprobados += 1
            listado_aprobado += line.strip() + "\t" + str(promedio_final) + "\n"

        elif (nota_par1 >= 4 and (nota_par2 >= 4 or nota_par3 >= 4)) or \
             (nota_par2 >= 4 and (nota_par1 >= 4 or nota_par3 >= 4)) or \
             (nota_par3 >= 4 and (nota_par1 >= 4 or nota_par2 >= 4)):
            cant_regulares += 1

        else:
            cant_libres += 1


    print(f"Porcentaje de libres: {cant_libres * 100 / contador_total } %")
    print(f"Porcentaje de regulares: {cant_regulares * 100 / contador_total } %")
    print(f"Porcentaje de promocionados: {cant_aprobados * 100 / contador_total } %")
    print(listado_aprobado)


if __name__ == "__main__":
    test()
