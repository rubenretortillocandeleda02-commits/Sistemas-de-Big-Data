import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Practica2/misiones_limpias.csv')

# Ejercicio 1. 
print(df.describe())

# Ejercicio 2-
plt.figure(figsize=(8, 6))
sns.boxplot(y=df["Nivel_Chakra"], color='orange')
plt.title('Nivel de chakra')
plt.show()

# Ejercicio 3.
Z = (df["Nivel_Chakra"] - df["Nivel_Chakra"].mean()) / df["Nivel_Chakra"].std()
for x in Z:
    if x >= 3 or x <= -3:
        print(x)
        
print(df[df["Nivel_Chakra"] == df["Nivel_Chakra"].max()])
.
# Ejercicio 4.
chakra_negativo = df[df["Nivel_Chakra"] < 0]
print(chakra_negativo)

print()

desconocida = df[df["Aldea"] == "Desconocida"]
print(desconocida)

print()

for x in Z:
    if x >= 2:
        print(x)
        
# Ejercicio 5.
sospechosos = [183, 268, 558, 699, 808, 899]
print(df[df["ID"].isin(sospechosos)])