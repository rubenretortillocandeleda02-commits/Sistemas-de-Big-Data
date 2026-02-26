import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("Practica 3/aptitudes_ninja.csv")

# 1. Exploración y limpieza.
print(df.isnull().sum())

print(df.duplicated().sum())

print(df.describe())


# 2. Encontrar el K óptimo.
# Escalado de datos
sc = StandardScaler() # Standardization
df[["fuerza_fisica", "control_chakra"]] = sc.fit_transform(df[["fuerza_fisica", "control_chakra"]])

X = df[['fuerza_fisica', 'control_chakra']]

# Método del codo.
sse = {}
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(X)
    X["clusters"] = kmeans.labels_
    sse[k] = kmeans.inertia_
plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.show()


# 3. Entrenamiento y clasificación.
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

df['clan_comportamiento'] = kmeans.fit_predict(X)

df.to_csv("Practica 3/aptitudes_ninja_final.csv")

print(df.head())

# 4. Mapa de especialidades.
mapa = sns.scatterplot(data = X,
                       x = "fuerza_fisica",
                       y = "control_chakra",
                       hue = df["clan_comportamiento"],
                       palette = "tab10")
sns.move_legend(
    mapa, "lower center",
    bbox_to_anchor=(.5, 1), ncol=3, title=None, frameon=False,
)

centroides = kmeans.cluster_centers_
plt.scatter(centroides[:, 0],centroides[:, 1], c='red', marker='X', s=200)
plt.show()
