import numpy as np

lista = []
for x in range(10):
    # Modificaciones master
    for y in lista:
        if y % x == 0:
            return y

print("Modificaciones script_1 master")
