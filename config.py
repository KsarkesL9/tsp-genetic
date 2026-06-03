SEED = 67
NUM_CITIES = 50

POPULATION_SIZE = 150
NUM_GENERATIONS = 20
NUM_PARENTS_MATING = 20

# metody selekcji :
# tournament - turniej losuje K osobnikow i wygrywa najlepszy TOURNAMENT_K kontroluje presje selekcyjna
# rws - ruletka szansa proporcjonalna do fitness moze dominowac jeden osobnik
# rank - ranking eliminuje problem dominacji ale ignoruje rzeczywiste wartosci fitness
# sss - steady-state zastepuje tylko najslabsze osobniki wolna ewolucja
# wybralem tournament bo daje kontrole nad presja selekcyjna i dobrze dziala przy duzych populacjach
PARENT_SELECTION = "tournament"
TOURNAMENT_K = 3

# metody krzyzowania:
# single_point - jeden punkt podzialu prosta i skuteczna dla permutacji
# two_points - dwa punkty wiecej wymian materialu genetycznego
# uniform - kazdy gen losowo od jednego z rodzicow duza roznorodnosc
# scattered - podobna do uniform ale bardziej losowa
CROSSOVER_TYPE = "single_point"

# metody mutacji:
# inversion - odwraca fragment trasy naturalna dla TSP bo zachowuje kolejnosc sasiadow
# swap - zamienia dwa geny miejscami prosta ale mniej efektywna dla TSP
# scramble - miesza losowy fragment bardziej agresywna niz inversion
MUTATION_TYPE = "inversion"
MUTATION_PERCENT_GENES = 3
