import pandas as pd
import sys

def main(ruta_lectura, ruta_escritura):
    df = pd.read_excel(ruta_lectura)


    df.to_excel(ruta_escritura)

if __name__ == "__main__":
    ruta_lectura, ruta_escritura = sys.argv[1], sys.argv[2]
    main(ruta_lectura, ruta_escritura)
