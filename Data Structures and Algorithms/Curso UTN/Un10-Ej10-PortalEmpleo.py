"""Un conocido portal de empleo requiere un programa para validar las búsquedas que se cargan en su página.
 Por cada búsqueda se requiere:

*CUIT: validar que sea un texto compuesto por 13 números separados por guiones de la siguiente manera: 00-00000000-0
*Descripción de la búsqueda: un texto donde cada palabra se separa con un espacio y termina con punto.
Debe tener un máximo de 60 caracteres y un mínimo de 3 palabras. Ninguna palabra debe contener dos mayúsculas seguidas.
*Salario ofrecido: controlar que sea un valor mayor a 0
Si todos los datos son válidos, mostrar el aviso completo. En caso contrario, informar que no es posible mostrarlo.

Para terminar, consultar al usuario si desea cargar otro aviso o salir del programa."""

#cuit = input("Ingrese cuit, con el formato 00-12345678-0: ") #13 caracteres

cuit = "20-32608635-6"
while len (cuit) != 13:
    print("formato incorrecto. Ingrese cuit nueveamente, son 11 numeros en total con 2 guiones."
          "\n Ejemplo: 20-32608635-6")
    cuit = input("Cuit: ")


busqueda = input("Descripcion del trabajo: ")
if busqueda[-1] != ".":
    busqueda += "."


# Contadores y restricciones
cp = cl = 0
largo_max = 60
palabras_minimas = 3

#Bandera
mayus1 = False
mayus2 = False

for car in busqueda:
    cl += 1
    if car != "." or car != " ":
        if "A" <= car <= "Z" and mayus1 == False and mayus2 == False:
            mayus1 = True
        else:
            if "A" <= car <= "Z" and mayus1 == True:
                mayus2 = True
                print("Una palabra contiene 2 mayusculas seguidas. Corrija \n")
            mayus1 = False

    if car == " " or car == "." and cl > 1:
        cp += 1
        cl = 0

if (len (busqueda) > largo_max) or (mayus2 == True) or (cp < palabras_minimas):
    print ("El anuncio no cumple con los requerimientos.")
    print (f"Largo max = {largo_max}, cant minima de palabras = {palabras_minimas}. Tampoco pueden haber 2 mayusculas"
           f" seguidas ")

    print(f"La cantidad de palabras es: {cp}, y la longitud es de {len(busqueda)}. Dos mayusculas seguidas: {mayus2}")

else:
    print(f"Cuit: {cuit}")
    print(f"Descripcion: {busqueda}")








