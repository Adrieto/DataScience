# Cuantos numeros menores que 904 son divisibles por 3?

nros = [i for i in range(10000)]
print(nros[-1])

cont= 0
for nro in nros:
    if nro % 5 == 0 and nro % 7 == 0 and nro % 10 == 0:
        cont += 1

print(cont)