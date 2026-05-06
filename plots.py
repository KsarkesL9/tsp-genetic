from matplotlib.pyplot import *

def draw_chart(model):
    history_list = []
    i = 0
    while i < len(model.best_solutions_fitness):
        history_list.append(-model.best_solutions_fitness[i])
        i += 1
    
    figure()
    plot(history_list)
    xlabel("Generacja")
    ylabel("Dlugosc trasy")
    grid(True)
    show()