import pandas as pd

# Datos: tiempos de espera en minutos
tiempos = [5, 8, 3, 10, 6, 9, 4, 7, 11, 2]

# Crear DataFrame
df = pd.DataFrame(tiempos, columns=["Minutos"])

# Calcular frecuencia
frecuencia = df["Minutos"].value_counts().sort_index()

# Calcular frecuencia acumulada
frecuencia_acumulada = frecuencia.cumsum()

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    "Minutos": frecuencia.index,
    "Frecuencia": frecuencia.values,
    "Frecuencia Acumulada": frecuencia_acumulada.values
})

# Mostrar la tabla
print(tabla_frecuencias)