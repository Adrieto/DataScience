
def prueba(n):
    r = ()
    for i in range(4, n+1, 5):
        r += i,
    return r
print(prueba(100))