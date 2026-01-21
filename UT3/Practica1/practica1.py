import pandas as pd
from datetime import datetime, timedelta

print("Iniciando limpieza de Rubén Retortillo Candeleda")

df = pd.read_csv("Practica1/ventas_big_data_ut3.csv")

total = len(df)

# 1. Eliminación de duplicados.
print(df.duplicated().sum())

df = df.drop_duplicates()

print()
print(df.duplicated().sum())

# 2. Normalización de productos.
print(df[118:123])

df["producto"] = df["producto"].str.strip()
df["producto"] = df["producto"].str.capitalize()

print()
print(df[118:123])

# 3. Tratamiento de precios.
print(df[2:8])

df["precio"] = df["precio"].apply(pd.to_numeric, errors='coerce')
df["precio"] = df["precio"].fillna(df["precio"].median())

print()
print(df[2:8])

# 4. Validación de cantidades.
negativos = (df["cantidad"] < 0).sum()

print(df[73:76])

df.loc[df["cantidad"] < 0, "cantidad"] = df["cantidad"].median()

print()
print(df[73:76])

# 5. Estandarización temporal.

print(df[5:9])

def fecha(valor):

    hoy = datetime.now().date()
    texto = str(valor).strip().lower()

    if texto == "ayer":
        return hoy - timedelta(days=1)

    if texto == "hace 2 dias":
        return hoy - timedelta(days=2)
    
    try:
        return pd.to_datetime(texto, format="mixed", dayfirst=True).date()
    except Exception:
        return pd.NaT

df["fecha"] = df["fecha"].apply(fecha)

print()
print(df[5:9])

# Bitácora
print(f"Filas iniciales: {total}")
print(f"Filas eliminadas por duplicidad: {total - len(df)}")
mediana = round(df["precio"].median(), 2)
print(f"Valor de la mediana de precios: {mediana}")
print(f"Número de registros con cantidades negativas descartados: {negativos}")

# JSON
df.to_json("Practica1/ventas_limpias_Ruben.json")
