import pandas as pd

# Datos: número de hijos por familia
hijos = [2, 1, 3, 0, 2, 4, 1, 2, 3, 1]

# Crear DataFrame
df = pd.DataFrame(hijos, columns=["Hijos"])

# Calcular frecuencia
frecuencia = df["Hijos"].value_counts().sort_index()

# Calcular frecuencia acumulada
frecuencia_acumulada = frecuencia.cumsum()

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    "Hijos": frecuencia.index,
    "Frecuencia": frecuencia.values,
    "Frecuencia Acumulada": frecuencia_acumulada.values
})

# Mostrar la tabla
print(tabla_frecuencias)