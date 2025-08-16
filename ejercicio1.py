import pandas as pd

# Lista de notas
notas = [75, 82, 90, 68, 75, 88, 92, 78, 85, 75]

# Crear DataFrame
df = pd.DataFrame(notas, columns=["Nota"])

# Calcular frecuencia
frecuencia = df["Nota"].value_counts().sort_index()

# Calcular frecuencia acumulada
frecuencia_acumulada = frecuencia.cumsum()

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    "Nota": frecuencia.index,
    "Frecuencia": frecuencia.values,
    "Frecuencia Acumulada": frecuencia_acumulada.values
})

# Mostrar la tabla
print(tabla_frecuencias)