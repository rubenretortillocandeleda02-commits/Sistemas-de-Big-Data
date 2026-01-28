import requests
import pandas as pd
import time

url = "https://pokeapi.co/api/v2/pokemon?limit=20"
todos_los_pokemon = []

while url:
    res = requests.get(url)
    data = res.json()
    todos_los_pokemon.extend(data['results'])
    url = data["next"]
    time.sleep(0.5)
    # print(url)

info_pokemon = []

for pokemon in todos_los_pokemon:
    url = pokemon["url"]
    res = requests.get(url)
    data = res.json()

    info_pokemon.append({
        "nombre": pokemon["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "experiencia_base": data["base_experience"],
        "bmi": round(((data["weight"] / 10) / (data["height"] / 10) ** 2), 2)
    })

df_pokemon = pd.DataFrame(info_pokemon)

print(df_pokemon.head())
