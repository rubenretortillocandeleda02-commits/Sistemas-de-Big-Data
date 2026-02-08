import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url_base = "https://coinmarketcap.com/?page={}"
lista_criptos = []

for i in range(1, 6): # Bucle para recorrer 5 páginas
    print(f"Procesando página {i}...")
    headers = { # Utilizo un user-agent para hacerme pasar por un busqueda normal
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0 ...'
    }
    response = requests.get(url_base.format(i), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    criptos = soup.select('table.cmc-table tbody tr') # Obtengo las filas de la tabla
    
    time.sleep(2)

    for moneda in criptos: # Recorro las filas obtenidas guardando los datos que quiero
        nombre_tag = moneda.find('p', class_='coin-item-name')
        nombre = nombre_tag.get_text(strip=True) if nombre_tag else None
        simbolo_tag = moneda.find('p', class_='coin-item-symbol')
        simbolo = simbolo_tag.get_text(strip=True) if simbolo_tag else None
        tds = moneda.find_all('td')
        precio = tds[3].get_text(strip=True) if len(tds) > 3 else None
        precio = precio.replace('$', '')
        precio = precio.replace(',', '')
        precio = float(precio)
        marketcap_tag = moneda.find('span', class_='sc-11478e5d-1 jfwGHx')
        marketcap = marketcap_tag.get_text(strip=True) if marketcap_tag else None
        if marketcap:
            marketcap = marketcap.replace('$', '')
            marketcap = marketcap.replace(',', '')
            marketcap = float(marketcap)
        volumen_tag = moneda.select_one('td p.font_weight_500')
        volumen = volumen_tag.get_text(strip=True) if volumen_tag else None
        if volumen:
            volumen = volumen.replace('$', '')
            volumen = volumen.replace(',', '')
            volumen = float(volumen)

        lista_criptos.append({ # Guardo los datos en la lista
            'Nombre': nombre,
            'Simbolo': simbolo,
            'Precio': precio,
            'Market cap': marketcap,
            'Volumen': volumen
        })
        

df = pd.DataFrame(lista_criptos) # Paso la lista de dataframe
df.to_csv('criptos.csv', index=False) # Guardo el dataframe como csv
print("Extracción de ejemplo completada.")
# Solo he conseguido sacar los datos de las 15 primeras monedas de clase página, pero el precio si sale de todas
