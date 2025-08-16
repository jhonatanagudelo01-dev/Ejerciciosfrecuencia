import pandas as pd

hijos = [2, 1, 3, 0, 2, 4, 1, 2, 3, 1]
df = pd.DataFrame(hijos, columns=["Hijos"])

frecuencia = df["Hijos"].value_counts().sort_index()
frecuencia_acumulada = frecuencia.cumsum()

tabla_frecuencias = pd.DataFrame({
    "Hijos": frecuencia.index,
    "Frecuencia": frecuencia.values,
    "Frecuencia Acumulada": frecuencia_acumulada.values
})

print(tabla_frecuencias)
    