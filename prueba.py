import requests
import hashlib
import pandas as pd
import numpy as np
import timeit
import sqlite3
import matplotlib as plt
import requests
from random import seed, randint

url = "https://restcountries-v1.p.rapidapi.com/all"
url2 = "https://restcountries.eu/rest/v2/all" 
headers = {
    'x-rapidapi-key': "f6252e6677msh4586e2a011b2ab8p1673cejsn6c68ed50e756",
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
variable=sorted(set(map(lambda x:x.get('region'),response.json())))
pais = requests.get(url2).json()
#print(pais[0])

cityName = [[] for _ in range(7)]
languageName = [[] for _ in range(7)]
time = [[] for _ in range(7)]

#print(variable)

for i in range(len(variable)):
    t0=timeit.timeit()
    for k in range(len(pais)):

        count = randint(0, len(pais)-1)
        if pais[count].get('region') == variable[i]:
            cityName[i] = pais[count].get('name')
            languageName[i]=hashlib.sha1(pais[count].get('languages')[0].get('name').encode('utf-8')).hexdigest()
        else:
            continue
    t1=timeit.timeit()
    time[i] = abs(round((t1-t0)*1000,3)) 

timeUnits = list(map(str, time))
timeUnits = list(map(lambda x: x + ' ms', timeUnits))
        


headings = ["Region", "City Name", "Languaje", "Time"]
df =pd.DataFrame(list(zip(variable, cityName, languageName, timeUnits)),columns=headings)
df.reset_index(drop=False)
df2 = pd.DataFrame(time)

#print(df)
tiempoTotal = round(float(df2.sum().array[0]),2)
media = round(float(df2.mean().array[0]),2)
minimo = round(float(df2.min().array[0]),2)
maximo = round(float(df2.max().array[0]),2)

# Solo se ejecuta una vez para crear la base de datos.

# conn = sqlite3.connect('test.db')
# df.to_sql('Nombre2', conn, index = False)
# conn.close()

#df.to_json(r'/home/ballesta/Documentos/proy/prueba1/data.json')




