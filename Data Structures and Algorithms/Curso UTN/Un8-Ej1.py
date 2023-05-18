opcion = input("ingrese una opcion: a, b o c: ")

cont_par = cont_impar = cont_pal_voc = 0
vocales = "aieouAEIOU"

if opcion == "a":
    n = int(input("ingrese un N para calcular la suma de cuadrados desde 1 hasta N: "))

    while n <= 0:
        print("El numero debe ser mayor que cero, reintente")

    suma_cuad = n*(n+1)*(2*n+1) / 6
    print(f"La suma de cuadrados de los primeros {n} numeros naturales es: {suma_cuad}")

elif opcion == "b":
    texto = input ('Ingrese un texto terminado con un ".": ')
    caracter_anterior = " "
    for caracter in texto:
        if caracter == " " or caracter == ".":
            if caracter_anterior in vocales:
                cont_pal_voc += 1
        caracter_anterior = caracter
    print(f"Las palabras finalizadas con vocales son: {cont_pal_voc}")

elif opcion == "c":
    n = int(input("ingrese un numero natural (Se corta con 0): "))
    while n != 0:
        if n%2 == 0:
            cont_par += 1
        else:
            cont_impar += 1

        n = int(input("ingrese un numero natural (Se corta con 0): "))

    if cont_par > cont_impar:
        print(f"la cantidad de pares es mayor a la de impares: {cont_par}>{cont_impar}")
    elif cont_par < cont_impar:
        print(f"la cantidad de impares es mayor a la de pares: {cont_impar}>{cont_par}")
    else:
        print(f"la cantidad de pares e impares son iguales: {cont_impar}={cont_par}" )

else:
    print("Se terminó lince")

