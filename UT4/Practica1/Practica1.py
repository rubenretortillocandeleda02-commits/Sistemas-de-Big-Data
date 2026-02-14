import pandas as pd

# 1. Carga del pergamino secreto
df = pd.read_csv('Practica1/registros_misiones.csv')

# --- SECCIÓN 1: LIMPIEZA DE DATOS ---

def limpiar_registro(df):
    """
    Reto 1: Elimina filas duplicadas.
    Reto 2: Estandariza la columna 'aldea' (quitar espacios, solventar mayúsculas/minúsculas).
    Reto 3: Si 'nin_id' es nulo y la 'aldea' es 'Kiri', rellena con 'Ninja de la Niebla Anonimo'.
    Reto 4: Convierte 'ts' a datetime.
    Reto 5: Filtra o corrige niveles de chakra imposibles (<= 0 o > 100.000).
    Reto 6: Renombra las columnas:
            'id_reg' -> 'ID', 'ts' -> 'Fecha', 'nin_id' -> 'Ninja', 'status' -> 'Estado', 'desc' -> 'Descripcion'
    """
    
    # Reto 1
    print(df.duplicated().sum())
    df = df.drop_duplicates()
    # print()
    # print(df.duplicated().sum())
    
    # Reto 2
    # print(df["aldea"].head(6))
    df["aldea"] = df["aldea"].str.replace(' ', '')
    df["aldea"] = df["aldea"].str.capitalize()
    df["aldea"] = df["aldea"].str.rstrip("_")
    # print()
    # print(df["aldea"].head(6))

    # Reto 3
    # print(df.loc[32:32, ["nin_id"]])
    df.loc[(df["nin_id"].isna()) & (df["aldea"] == "Kiri"), "nin_id"] = "Ninja de la Niebla Anonimo"
    # print()
    # print(df.loc[32:32, ["nin_id"]])

    # Reto 4
    # print(df.info())
    df["ts"] = pd.to_datetime(df["ts"])
    # print(df.info())

    # Reto 5
    # print(df.loc[[2, 31], ["chakra"]])
    mediana = df.loc[(df["chakra"] > 0) & (df["chakra"] <= 100000), "chakra"].median()
    df.loc[(df["chakra"] <= 0) | (df["chakra"] > 100000) | (df["chakra"].isna()), "chakra"] = mediana
    # print(df.loc[[2, 31], ["chakra"]])

    # Reto 6
    # print(df.info())
    df = df.rename(columns={"id_reg": "ID", "ts": "Fecha", "nin_id": "Ninja", "status": "Estado", "desc": "Descripcion"})
    # print(df.info())

    return df

# --- SECCIÓN 2: BÚSQUEDA Y CONSULTAS ---

def realizar_consultas(df):
    """
    Reto 7: Busca descripciones con las palabras 'espía', 'sospechoso' o 'enemigo'.
    Reto 8: Filtra ninjas de la 'Aldea de la Lluvia' (Amegakure) con chakra > 5000 y rango != 'D'.
    Reto 9: Encuentra los accesos ocurridos de madrugada (entre las 23:00 y las 05:00).
    Reto 10: Obtén el Top 5 ninjas con más chakra de cada aldea.
    Reto 11: Lista misiones de ninjas que NO pertenecen a la alianza (Konoha, Suna, Kumo).
    Reto 12: Cuenta cuántas misiones de estado 'Fallo' hay por cada aldea.
    """
    
    # Reto 7
    # print(df.loc[df["Descripcion"].str.contains("espía|sospechoso|enemigo"), "Descripcion"])

    # Reto 8
    # ninjas = df[(df["aldea"] == "Amegakure") & (df["chakra"] > 5000) & (df["rango"] != "D")]
    # print(ninjas)

    # Reto 9
    # accesos = df[(df["Fecha"].dt.hour >= 23)|(df["Fecha"].dt.hour < 5)]
    # print(accesos)
    
    # Reto 10
    # aldeas = df["aldea"].unique()
    # for aldea in aldeas:
    #     print(df[df["aldea"] == aldea].sort_values(by="chakra", ascending=False).head(5))
    #     print()
    
    # Reto 11
    # misiones = df.loc[(df["aldea"] != "Konoha") & (df["aldea"] != "Suna") & (df["aldea"] != "Kumo"), "Descripcion"].unique()
    # for mision in misiones:
    #     print(mision)
    
    # Reto 12
    aldeas = df["aldea"].unique()
    for aldea in aldeas:
        print(aldea)
        print(df.loc[(df["aldea"] == aldea) & (df["Estado"] != "Fallo"), "Descripcion"].count())
        print()

    pass

# --- EJECUCIÓN DEL PROTOCOLO ANBU ---
print("Iniciando Rastreo de Chakra de Rubén...")
df_limpio = limpiar_registro(df)
realizar_consultas(df_limpio)
df_limpio.to_csv('Practica1/misiones_limpias_Ruben.csv', index=False)