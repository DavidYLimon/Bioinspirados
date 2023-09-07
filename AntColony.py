""" 
Ant Colony inspirado en el comportamiento de las homigas,

- inicializacion: cada hormiga da el rol por toda la ciudad pero regresa al punto de partida (o se puede referir a una posible ruta pal rol)
- Exploracion: Cada hormiga decide que ruta tomar dependiendo de feromonas de la ruta 
- Deposicion de feromanas : a lo largo de los ciclos las hormigas toman una ruta y al tomarla dejan feromonas a la ruta mas optima y asi generar como un mapa de la mejor ruta posible 
- Evaporacionde feromonas : no permite que las feromonas de las hormigas se almacenene por mucho tiempo, lo que obliga a generar nuevas y mejores rutas 
- Mejora de la solucion : al terminal el numero de iteraciones la mejor solucion hasta el momento es la mas aproximada al problema 
"""

import random

# Parámetros del algoritmo
num_ciudades = 10
num_hormigas = 5
iteraciones = 100
tasa_evaporacion = 0.5
alfa = 1.0  # Peso de las feromonas
beta = 2.0  # Peso de la heurística

# Matriz de distancias entre ciudades (aquí puedes definir tu propio grafo)
distancias = [[0, 29, 20, 21, 16, 31, 100, 12, 4, 31],
              [29, 0, 15, 18, 12, 27, 10, 25, 13, 17],
              [20, 15, 0, 28, 7, 19, 21, 8, 26, 11],
              [21, 18, 28, 0, 18, 8, 12, 14, 24, 19],
              [16, 12, 7, 18, 0, 12, 14, 9, 19, 13],
              [31, 27, 19, 8, 12, 0, 24, 13, 10, 17],
              [100, 10, 21, 12, 14, 24, 0, 16, 15, 11],
              [12, 25, 8, 14, 9, 13, 16, 0, 22, 28],
              [4, 13, 26, 24, 19, 10, 15, 22, 0, 23],
              [31, 17, 11, 19, 13, 17, 11, 28, 23, 0]]

# Inicialización de feromonas en las aristas
feromonas = [[1.0 for _ in range(num_ciudades)] for _ in range(num_ciudades)]

# Función de probabilidad para elegir la siguiente ciudad
def calcular_probabilidades(ciudad_actual, ciudades_no_visitadas):
    probabilidades = []
    suma_probabilidades = 0.0

    for ciudad in ciudades_no_visitadas:
        feromona = feromonas[ciudad_actual][ciudad]
        heuristica = 1.0 / distancias[ciudad_actual][ciudad]
        probabilidad = (feromona ** alfa) * (heuristica ** beta)
        probabilidades.append(probabilidad)
        suma_probabilidades += probabilidad

    # Normalizar probabilidades
    probabilidades = [p / suma_probabilidades for p in probabilidades]
    
    return probabilidades

# Función para elegir la siguiente ciudad
def elegir_siguiente_ciudad(ciudad_actual, ciudades_no_visitadas):
    probabilidades = calcular_probabilidades(ciudad_actual, ciudades_no_visitadas)
    return random.choices(ciudades_no_visitadas, probabilidades)[0]

# Función para recorrer una ruta con una hormiga
def recorrer_ruta(ciudades):
    ciudad_actual = random.randint(0, num_ciudades - 1)
    ruta = [ciudad_actual]
    ciudades_no_visitadas = list(range(num_ciudades))
    ciudades_no_visitadas.remove(ciudad_actual)

    while ciudades_no_visitadas:
        siguiente_ciudad = elegir_siguiente_ciudad(ciudad_actual, ciudades_no_visitadas)
        ruta.append(siguiente_ciudad)
        ciudades_no_visitadas.remove(siguiente_ciudad)
        ciudad_actual = siguiente_ciudad

    return ruta

# Función para calcular la longitud de una ruta
def calcular_longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancias[ruta[i]][ruta[i + 1]]
    longitud += distancias[ruta[-1]][ruta[0]]  # Volver al punto de inicio
    return longitud

# Ciclo principal del algoritmo
for _ in range(iteraciones):
    rutas_hormigas = []

    # Construir soluciones con las hormigas
    for _ in range(num_hormigas):
        ruta_hormiga = recorrer_ruta(list(range(num_ciudades)))
        rutas_hormigas.append(ruta_hormiga)

    # Evaluar las soluciones y encontrar la mejor
    mejor_ruta = min(rutas_hormigas, key=calcular_longitud_ruta)
    mejor_longitud = calcular_longitud_ruta(mejor_ruta)

    # Actualizar feromonas
    for i in range(num_ciudades):
        for j in range(num_ciudades):
            if i != j:
                feromonas[i][j] *= (1.0 - tasa_evaporacion)
                if i in mejor_ruta and j in mejor_ruta:
                    feromonas[i][j] += (1.0 / mejor_longitud)

# Encontrar la mejor solución global
mejor_ruta_global = min(rutas_hormigas, key=calcular_longitud_ruta)
mejor_longitud_global = calcular_longitud_ruta(mejor_ruta_global)

print("Mejor ruta encontrada:", mejor_ruta_global)
print("Longitud de la mejor ruta:", mejor_longitud_global)
