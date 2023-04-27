"""Se vota una ley en el Senado, y se ingresan votos a favor, en contra
 y abstenciones de los senadores presentes.

Informar cuál fue el resultado de la votación. Si la ley fue aprobada,
indicar si fue por mayoría absoluta (los votos afirmativos superan a
la suma de los negativos más las abstenciones) o por mayoría simple
(los votos afirmativos superan a los negativos, sin tener en cuenta las
abstenciones). También informar en caso de que la ley sea rechazada.

Por último, considerando que la Cámara está formada por 72 senadores,
determinar cuantos se encontraban ausentes."""
bancada = 72
votos_favor = int(input("Votos positivos: "))
votos_contra = int(input("Votos negativos: "))
abstenciones = int(input("Abstenciones: "))
ausencias = bancada - votos_contra - votos_favor - abstenciones 

simple = votos_favor - votos_contra
absoluta = simple - abstenciones
print("simple:", simple, "   Absoluto: ", absoluta)
if simple > 0:
    if absoluta > 0:
        mayoria = "absoluta"
    else:
        mayoria = "simple"
    print(f"\nLey aprobada por mayoria {mayoria}, con {votos_favor} votos a favor, "
           f"{votos_contra} votos en contra y {abstenciones} abstenciones")
else:
    print (f"Ley rechazada con {votos_favor} votos a favor,"
           f"{votos_contra} votos en contra y {abstenciones} abstenciones")

print(f"Ausencias en el recinto: {ausencias} senadores")