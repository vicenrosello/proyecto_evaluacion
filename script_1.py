import numpy as np
from setup.tools import reduce

lista = []

# Modificaciones ingestas
df = reduce(lambda left, right: pd.concat([left, right]), lista)

print("Modificaciones script_1 ingestas")
