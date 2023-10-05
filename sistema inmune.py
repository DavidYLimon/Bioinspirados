import random

def fitness(solution):
    return -sum(x ** 2 for x in solution)


def initialize_population(population_size, solution_size):
    population = []
    for _ in range(population_size):
        solution = [random.uniform(-5, 5) for _ in range(solution_size)]  
        population.append(solution)
    return population


def select_antibodies(population, num_selected):
    sorted_population = sorted(population, key=fitness, reverse=True)
    return sorted_population[:num_selected]


def clone_and_mutate(antibodies, mutation_rate):
    new_population = []
    for antibody in antibodies:
        new_antibody = [x + random.uniform(-mutation_rate, mutation_rate) for x in antibody]
        new_population.append(new_antibody)
    return new_population


population_size = 50
solution_size = 10
num_generations = 100
num_selected = 10
mutation_rate = 0.1


population = initialize_population(population_size, solution_size)


for generation in range(num_generations):

    fitness_values = [fitness(solution) for solution in population]

    selected_antibodies = select_antibodies(population, num_selected)

    population = clone_and_mutate(selected_antibodies, mutation_rate)

    best_solution = max(population, key=fitness)
    best_fitness = fitness(best_solution)
    print(f"Generación {generation + 1}: Mejor aptitud = {best_fitness}")

best_solution = max(population, key=fitness)
best_fitness = fitness(best_solution)
print("Mejor solución encontrada:", best_solution)
print("Mejor aptitud:", best_fitness)
