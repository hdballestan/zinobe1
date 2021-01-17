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






#datos=[tiempoTotal,media,minimo,maximo]
#print(datos)
#print(timeUnits)
#
        # print(count)
# print(cityName)

#Vector auxiliar con países por región al azar


# variable_df = pd.DataFrame.from_dict(variable)
# variable_df.plot(kind='line')
#print(response.text)

# #__________________________________________________________________________________
# t1=time.time() #Intento fallido de calcular el tiempo
# #__________________________________________________________________________________
# url = "https://restcountries-v1.p.rapidapi.com/all"
# url2 = "https://restcountries.eu/rest/v2/all"
# #_________________________ Obtener las regiones ___________________________________
# headers = {
#     'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
#     'x-rapidapi-key': "2cc28d668cmshc5fdafc4036da01p112433jsn24c636fdcbdb"
#     }

# response = requests.request("GET", url, headers=headers)
# variable = response.json()

# regiones=sorted(set(map(lambda x:x.get('region'),variable)))
# response.close()
# #print(regiones) test
# #_________________________ Obtener los países e idiomas ___________________________
# pais = requests.get(url2).json()
# #type(pais)
# count = 0
# cityName = [[] for _ in range(7)] # al parecer no puedo crear una lista vacía sin más
# languageName = [[] for _ in range(7)]
# tiime = [[] for _ in range(7)]
# for i in range(len(pais)):
#     if pais[i].get('region') == regiones[count]:
#         cityName[count] = pais[i].get('name')
#         #languageName[count]=pais[i].get('languages')[0].get('name')#sin cifrar
#         languageName[count]=hashlib.sha1(pais[i].get('languages')[0].get('name').encode('utf-8')).hexdigest()#cifrada
#         count +=1
#         continue    

# #print(cityName[0]) #test
# #print(languageName[0]) #test
# #_________________________ crear la tabla _______________________________________

# for t in range(len(tiime)):
#     tiime[t] = 'nan'

# header = ['Region', 'City Name', 'language', 'time']

# filas = [regiones, cityName, languageName, tiime]

# #print(filas)
# dic = {}
# x=0
# for h in header:
#     dic[h]=filas[x]
#     x+=1

# t2=time.time() - t1 #por la forma en que construí la tabla todas las filas se hacen al mismo tiempo Y_Y *arreglar
# tabla_df = pd.DataFrame(dic)
# tabla_df.time = tabla_df.time.replace({"nan": t2})
# #print(dic) #Test
# #________________________Archivo .Json provicional_______________________________

# #filename = "C:\\Users\\sandrapdiaz\\Documents\\python problem\\tablaL1"


# #tabla_df.to_json(filename + ".json")

# #_____________________promedios de la tabla de tiempo y percentiles_______________
# #print(tabla_df.time.describe())

# #print(tabla_df)


# #___________________________________Gestión de sql____________________________________________

# from pandas import DataFrame

# conn = sqlite3.connect('Test32.db')
# c = conn.cursor()

# c.execute('CREATE TABLE  Convert4 (Region text, City Name text, Language text, Time text)')
# conn.commit()
# df = DataFrame(dic, columns= ['Region', 'City Name', 'Language', 'Time'])

# #tabla_df.to_sql(name='Convert4', con=conn, if_exists='append', index = False) #Línea que no funciona
# #Error radica en la forma en que se construyó la tabla - status = dumb