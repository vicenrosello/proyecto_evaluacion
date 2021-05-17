import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_models import LinearRegression

df = pd.read_csv("fichero.csv", sep = ";")

x_train, x_test, y_train, y_test = train_test_split(df['texto'], df['etiqueta'], train_size = 0.8)

## Añadir el entrenamiento de un modelo de regresion lineal
