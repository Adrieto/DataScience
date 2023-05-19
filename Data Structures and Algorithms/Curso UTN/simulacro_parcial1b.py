import random
random.seed(20220512)

lim_inf = 1
lim_sup = 45000
cant = 25000

cont_3 = cont_5 = cont_ninguno = cont_2_11 = 0
acum_2_11 = 0
mayor = 0

for i in range (cant):
    n = random.randint(lim_inf,lim_sup)

    if n % 3 == 0:
        cont_3 += 1
    elif n % 5 == 0:
        cont_5 += 1
    else:
        cont_ninguno += 1

    aux = str(n)
    if aux[0] == "1" and n > mayor:
        mayor = n
    
    if n % 2 == 0 and n % 11 == 0:
        cont_2_11 += 1
        acum_2_11 += n

porcentaje_imp_11 = acum_2_11 // cont_2_11 
porcentaje_3 = (cont_3 * 100) // cant
porcentaje_5 = (cont_5 * 100) // cant
porcentaje_ninguno = (cont_ninguno * 100) // cant

print (f"Control, total debe ser {cant}. Total: {cont_3+cont_5+cont_ninguno}")
print (f"Multiplos de 3: {cont_3}")
print (f"Multiplos de 5: {cont_5}")
print ()
print (f"Ni multiplos de 3 ni de 5: {cont_ninguno}")
print (f"Mayor numero con primer digito igual a 1: {mayor}")
print ()
print (f"promedio de los pares multiplos de 11: {porcentaje_imp_11}")
print (f"porcentajes multipos 3, multiplo 3 y no 5, ni de 3 ni de 5: ")
print (f"{porcentaje_3},{porcentaje_5},{porcentaje_ninguno},")


