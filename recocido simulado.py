import random
import math

# Problema de la mochila
pesos = [2, 3, 5, 7, 9]
valores = [6, 8, 12, 15, 20]
capacidad_mochila = 15

# Parámetros del algoritmo de recocido simulado
temperatura_inicial = 1000
factor_enfriamiento = 0.85
iteraciones_por_temperatura = 1000

# Función para calcular el valor total de una solución
def valor_total(solucion):
    valor = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            valor += valores[i]
    return valor

# Función para generar una solución vecina
def generar_vecino(solucion):
    vecino = list(solucion)
    indice = random.randint(0, len(vecino) - 1)
    vecino[indice] = 1 - vecino[indice]  # Cambia de 0 a 1 o de 1 a 0
    return vecino

# Algoritmo de recocido simulado
solucion_actual = [random.randint(0, 1) for _ in range(len(pesos))]
temperatura_actual = temperatura_inicial

mejor_solucion = list(solucion_actual)
mejor_valor = valor_total(solucion_actual)

while temperatura_actual > 1:
    for _ in range(iteraciones_por_temperatura):
        vecino = generar_vecino(solucion_actual)
        delta = valor_total(vecino) - valor_total(solucion_actual)
        if delta > 0 or random.random() < math.exp(delta / temperatura_actual):
            solucion_actual = list(vecino)
            valor_actual = valor_total(solucion_actual)
            if valor_actual > mejor_valor:
                mejor_solucion = list(solucion_actual)
                mejor_valor = valor_actual

    temperatura_actual *= factor_enfriamiento

print("Mejor solución encontrada:", mejor_solucion)
print("Valor total de la mochila:", mejor_valor)
