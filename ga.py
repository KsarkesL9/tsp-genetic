import pygad

from config import (
    POPULATION_SIZE,
    NUM_GENERATIONS,
    NUM_PARENTS_MATING,
    PARENT_SELECTION,
    TOURNAMENT_K,
    CROSSOVER_TYPE,
    MUTATION_TYPE,
    MUTATION_PERCENT_GENES,
)

def count_distance(answer, table):
    n = len(answer)
    total = 0
    i = 0
    while i < n - 1:
        total += table[answer[i]][answer[i + 1]]
        i += 1
    total += table[answer[-1]][answer[0]]
    return total

def start(table, seed_num):
    n = len(table)
    best_solutions_history = []

    def check_fitness(model, answer, index):
        return -count_distance(answer, table)

    def on_generation(model):
        best = model.best_solution()[0]
        best_solutions_history.append(list(best))

    ga_obj = pygad.GA(
        num_generations=NUM_GENERATIONS,
        num_parents_mating=NUM_PARENTS_MATING,
        fitness_func=check_fitness,
        sol_per_pop=POPULATION_SIZE,
        num_genes=n,
        gene_space=list(range(n)),
        gene_type=int,
        allow_duplicate_genes=False,
        parent_selection_type=PARENT_SELECTION,
        K_tournament=TOURNAMENT_K,
        crossover_type=CROSSOVER_TYPE,
        mutation_type=MUTATION_TYPE,
        mutation_percent_genes=MUTATION_PERCENT_GENES,
        random_seed=seed_num,
        suppress_warnings=True,
        on_generation=on_generation,
    )
    ga_obj.run()
    return ga_obj, best_solutions_history
