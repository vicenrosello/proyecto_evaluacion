import numpy as np
import pandas as pd
import dask.dataframe as ddf

lista = []
for x in range(10):
    # Nuevas modificaciones
    df = ddf.read_excel("*.xlsx")

print("Nuevas Modificaciones script_1 master")
