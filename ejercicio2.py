import pandas as pd

# Datos: edades de las personas
edades = [25, 30, 22, 28, 35, 27, 31, 29, 26, 33]

# Crear DataFrame
df = pd.DataFrame(edades, columns=["Edad"])

# Calcular frecuencia
frecuencia = df["Edad"].value_counts().sort_index()

# Calcular frecuencia acumulada
frecuencia_acumulada = frecuencia.cumsum()

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    "Edad": frecuencia.index,
    "Frecuencia": frecuencia.values,
    "Frecuencia Acumulada": frecuencia_acumulada.values
})

# Mostrar la tabla
print(tabla_frecuencias)