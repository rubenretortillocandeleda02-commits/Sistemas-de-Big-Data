# Práctica 2: El pergamino infinito - Consumo de APIs.
En esta práctica obtendremos información de la PokéAPI para obtener información que luego transformaremos y almacenaremos en un dataset.

## Evidencias de la invocación.
Bucle que recorre las páginas para recolectar la información.

```
while url:
    res = requests.get(url)
    data = res.json()
    todos_los_pokemon.extend(data['results'])
    url = data["next"]
    time.sleep(0.5)
    print(url)
```

<img src="/imagenes/1.png"></img>

<br></br>

## Evicencias de la transformación.
Bucle que almacena la información y calcula el bmi.

```
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
```

<img src="/imagenes/2.png"></img>

<br></br>

## Preguntas de reflexión.
**1. ¿Por qué es importante actualizar la URL con el enlace next en lugar de simplemente incrementar un número de página manualmente?**
Si aumentamos el número manualmente tendríamos que saber cuál es el número total de páginas, pero con el enlace next el bucle para cuando llega a la última, sean 10 o 1000.

**2. ¿Qué ventaja tiene normalizar las unidades (como pasar de decímetros a metros) dentro del propio proceso ETL en lugar de hacerlo después en una hoja de cálculo?**
La ventaja es que ya se tendrían todos los datos de forma estandarizada guardados en la base de datos o en un archivo en vez de tener que volver a modificarlos para volver a guardarlos.

**3. Si la API tuviera un límite de 1000 registros por página, ¿cómo afectaría esto al rendimiento de tu script?**
Probablemente haría que la API fuese más lento o que dejara de funcionar.

## Conclusión
Las extracción automática de datos tiene muchas ventajas frente a la descarga manual de archivo como puede ser la automatización, la escalabilidad o evitar el error humano.