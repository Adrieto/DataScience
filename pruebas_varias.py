import random

x = [round((0.081 + random.random() * (0.55 - 0.081)), 3) for i in range(0, 20)]


print(x)
