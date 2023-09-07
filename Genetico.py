import random

# Función objetivo: x^2 + 2
def fitness_function(x):
    return x**2 + 2

# Genera un individuo aleatorio de 4 bits
def generate_individual():
    return [random.randint(0, 1) for _ in range(4)]

# Calcula la aptitud de un individuo
def calculate_fitness(individual):
    # Convierte el valor binario a decimal
    x = sum(bit * (2**i) for i, bit in enumerate(reversed(individual)))
    return fitness_function(x)

# Función de cruce (mezcla) para dos individuos
def crossover(parent1, parent2):
    # Elije un punto de cruce aleatorio
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Realiza el cruce
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2

# Función de mutación con un porcentaje de posibilidad configurable
def mutate(individual, mutation_rate):
    mutated_individual = []
    for bit in individual:
        if random.random() < mutation_rate:
            mutated_bit = 1 - bit  # Cambia 0 a 1 o viceversa con la probabilidad de mutación
        else:
            mutated_bit = bit
        mutated_individual.append(mutated_bit)
    return mutated_individual

# Genera una población inicial de 30 individuos
initial_population = [generate_individual() for _ in range(30)]

# Evalúa la aptitud de cada individuo en la generación inicial y almacena el mejor individuo
best_individual_initial = None
best_fitness_initial = float('-inf')

# Imprime cada individuo y su aptitud en la generación inicial
print("Generación Inicial\n")
for i, individual in enumerate(initial_population):
    fitness = calculate_fitness(individual)
    print(f"Individuo {i + 1}: {individual}, Aptitud: {fitness}")
    if fitness > best_fitness_initial:
        best_fitness_initial = fitness
        best_individual_initial = individual

# Imprime el mejor individuo y su aptitud en la generación inicial
print("\nMejor individuo en la Generación Inicial:", best_individual_initial)
print("Su Aptitud:", best_fitness_initial)

# Realiza el cruce (mezcla) en la segunda generación
print("\nCruce (Mezcla) en la Segunda Generación\n")
new_population = []
for i in range(15):
    # Selecciona dos padres aleatorios de la población inicial
    parent1 = random.choice(initial_population)
    parent2 = random.choice(initial_population)
    
    # Realiza el cruce para obtener dos hijos
    child1, child2 = crossover(parent1, parent2)
    
    # Agrega los hijos a la población de mezcla
    new_population.append(child1)
    new_population.append(child2)

# Evalúa la aptitud de cada individuo en la población resultante del cruce y encuentra al mejor individuo
best_individual_mixed = None
best_fitness_mixed = float('-inf')

# Imprime la población resultante del cruce
print("\nPoblación Resultante del Cruce\n")
for i, individual in enumerate(new_population):
    fitness = calculate_fitness(individual)
    print(f"Individuo {i + 1}: {individual}, Aptitud: {fitness}")
    if fitness > best_fitness_mixed:
        best_fitness_mixed = fitness
        best_individual_mixed = individual

# Imprime el mejor individuo y su aptitud en la población resultante del cruce
print("\nMejor individuo en la Población Resultante del Cruce:", best_individual_mixed)
print("Su Aptitud:", best_fitness_mixed)

# Porcentaje de mutación (ajustable)
mutation_rate = 0.1  # Puedes cambiar este valor según sea necesario

# Aplica mutación a la población de mezcla
print("\nMutación en la Tercera Generación (Población de Mezcla)\n")
mixed_population = []
for i in range(len(new_population)):
    mixed_population.append(mutate(new_population[i], mutation_rate))

# Evalúa la aptitud de cada individuo en la población con mutación y encuentra al mejor individuo
best_individual_mutation = None
best_fitness_mutation = float('-inf')

# Imprime la población con mutación
print("\nPoblación con Mutación\n")
for i, individual in enumerate(mixed_population):
    fitness = calculate_fitness(individual)
    print(f"Individuo {i + 1}: {individual}, Aptitud: {fitness}")
    if fitness > best_fitness_mutation:
        best_fitness_mutation = fitness
        best_individual_mutation = individual

# Imprime el mejor individuo y su aptitud en la población con mutación
print("\nMejor individuo en la Población con Mutación:", best_individual_mutation)
print("Su Aptitud:", best_fitness_mutation)

