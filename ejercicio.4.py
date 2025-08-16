import pandas as pd

# Datos: estaturas en centímetros
estaturas = [175, 180, 172, 185, 178, 190, 182, 177, 188, 183]

# Crear DataFrame
df = pd.DataFrame(estaturas, columns=["Estatura"])

# Calcular frecuencia
frecuencia = df["Estatura"].value_counts().sort_index()

# Calcular frecuencia acumulada
frecuencia_acumulada = frecuencia.cumsum()

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    "Estatura (cm)": frecuencia.index,
    "Frecuencia": frecuencia.values,
    "Frecuencia Acumulada": frecuencia_acumulada.values
})

# Mostrar la tabla
print(tabla_frecuencias)