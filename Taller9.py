import requests

URL = 'https://swapi.dev/api/planets/'

data = requests.get(URL)
data = data.json()
Resultados_Planetas = []

for i in range(1, 61):
    URL = URL + str(i)
    data = requests.get(URL)
    data = data.json()
    Info = (data['climate'], data['films'])
    Resultados_Planetas.append(Info)
    URL = 'https://swapi.dev/api/planets/'

# a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?,

Peliculas_Planetas_Aridos = []

for element in Resultados_Planetas:
    if ('arid' in element[0]) == True:
        Peliculas_Planetas_Aridos.append(element[1])

Lista_Peliculas_Planetas_Aridos = []
for element in Peliculas_Planetas_Aridos:
    for peliculas in element:
        if (peliculas not in Lista_Peliculas_Planetas_Aridos) == True:
            Lista_Peliculas_Planetas_Aridos.append(peliculas)

print('Existen', len(Lista_Peliculas_Planetas_Aridos), 'peliculas donde aparecen planetas áridos en la saga.')


# ¿Cuántos Wookies aparecen en la sexta película?

l_wookies = []
i = 0

if i == 6:
    personajes = data['characters']
    for personaje in personajes:
        p = requests.get(personaje)
        d = p.json()
        especies = d['species']
        for especie in especies:
            p2 = requests.get(especie)
            d2 = p2.json()
            if str(d2["name"]) == 'Wookie':
                l_wookies.append(str(d["name"]))


# ¿Cuál es el nombre de la aeronave más grande en toda la saga?

URL = 'https://swapi.dev/api/vehicles/4'
data = requests.get(URL)
data = data.json()
Aeronaves = []

for i in range(1, 40):
    try:
        URL = 'https://swapi.dev/api/vehicles/'
        URL = URL + str(i)
        dataV = requests.get(URL)
        dataV = dataV.json()
        Info = (dataV['name'], dataV['length'])
        Aeronaves.append(Info)
    except:
        print('No se han encontrado')