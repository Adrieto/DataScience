def comparacion(a, b):
    if b == 0:
        return False
    elif a == 0:
        return True
    else:
        return comparacion(a-1, b-1)
    

print(comparacion(400,300))