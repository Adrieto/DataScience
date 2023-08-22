def search_dot(iterable):
    # Look for the index in which we have "."
    iterable_string = str(iterable)
    for i in range (len(iterable_string)):
        if "." == iterable_string[i]:
            return i
        
def divisiones_sucesivas(parte_entera, base):
    cociente = parte_entera
    resultado = ""

    while True:
        resultado += str(cociente % base)
        cociente //= base  
        if cociente < base:        
            resultado += str(cociente)
            break
    #Finalmente, se invierte la lista, para devolver el resultado correcto
    resultado = resultado [-1::-1]    
    return resultado

def multiplicaciones_sucesivas(parte_fraccionaria, base):
    fraccion = float("0." + str(parte_fraccionaria))
    resultado = ""

    cont_iters = 0
    max_iter = 8

    while cont_iters <= max_iter:
        fraccion = (fraccion*base)
        #Se guarda la parte entera solamente
        resultado += str(int(fraccion))

        cont_iters += 1
        if abs(int(fraccion) - fraccion) <= 1e-6: #Quiebro si la diferencia es muy pequeña
            break
        if fraccion > 1.0:
            fraccion = round(fraccion - 1.0, 5)      
    return resultado  


def dec2binary(n_decimal, base):

    parte_entera = int(n_decimal)
    posicion_coma = search_dot(n_decimal)
    parte_fraccionaria = int(str(n_decimal)[(posicion_coma+1):])
    
    #Parte entera: Divisiones sucesivas
    resultado_entero = divisiones_sucesivas(parte_entera, base)
    #Parte fraccionaria: multiplicaciones sucesivas
    resultado_fraccionario = multiplicaciones_sucesivas(parte_fraccionaria, base)
    
    return resultado_entero + "." + resultado_fraccionario




numero_prueba = 25.78

n_en_binario = dec2binary(numero_prueba, 2)
print("\n", n_en_binario)

#Prueba de division
#print (divisiones_sucesivas(25,2))
#print(multiplicaciones_sucesivas(78,2))