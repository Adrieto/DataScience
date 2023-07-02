def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int (3*n + 1)

def promedio (lista):
    total = 0
    for idx, valor in enumerate(lista):
        total += valor
    return (total / len(lista))

def test():
    n = 9386

    orbita_collatz = [n]

    while n != 1:
        n = collatz(n)
        orbita_collatz.append(n)

    longitud_orbita = len(orbita_collatz)

    print (orbita_collatz)
    print(f"Longitud de la orbita: {longitud_orbita}")
    print(f"Promedio de la orbita: {promedio(orbita_collatz)}")
    print(f"Mayor numero de la orbita: {max(orbita_collatz)}")

    # {13251, 234519, 9386}

if __name__ == "__main__":
    test()