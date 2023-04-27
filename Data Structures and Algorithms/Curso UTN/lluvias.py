"""En una localidad nos piden que realicemos un análisis de las lluvias 
caídas en un trimestre (3 cantidades).
Para ello se debe ingresar por teclado la cantidad de milímetros caídos
por mes y con dichos datos resolver lo siguiente:
Promedio de milímetros caídos.
Cantidad de meses con más o igual lluvia que el promedio.
Mes con menos lluvias en el trimestre.
Si dicho mes tuvo 0 mm caídos indicar con un mensaje."""

lluvia1 = int(input("ingrese cantidad de lluvia 1 en mm: "))
lluvia2 = int(input("ingrese cantidad de lluvia 2 en mm: "))
lluvia3 = int(input("ingrese cantidad de lluvia 3 en mm: "))

promedio = (lluvia1 + lluvia2 + lluvia3) / 3

meses_lluviosos = 0
if lluvia1 >= promedio:
    meses_lluviosos += 1
if lluvia2 >= promedio:
    meses_lluviosos += 1
if lluvia3 >= promedio:
    meses_lluviosos += 1

menor_lluvia = min (lluvia1, lluvia2, lluvia3)

#mes_menos_lluvia
if lluvia1 < lluvia2  and lluvia1 < lluvia3:
    mes_menor = 1
    menor_lluvia = lluvia1
elif lluvia2 <  lluvia3:
    mes_menor = 2
    lluvia_menor = lluvia2
else:
    mes_menor = 3
    lluvia_menor = lluvia3

print (f"El mes con menos lluvia fue el: {mes_menor}")
print (f"lluvias promedio: {promedio}")
print (f"Cantidad de meses con mas o igual lluvia que el promedio: {meses_lluviosos}")

if menor_lluvia == 0:
    print (f"El mes de menos lluvia cayeron {menor_lluvia} mm")
else:
    print (f"menor lluvia: {menor_lluvia}" )