from matplotlib.pyplot import *
from matplotlib.animation import FuncAnimation

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

def draw_path_animation(coords, history):
    xs = []
    ys = []
    i = 0
    while i < len(coords):
        xs.append(coords[i][0])
        ys.append(coords[i][1])
        i += 1

    fig, ax = subplots()

    def update(gen):
        ax.clear()
        tour = history[gen]

        tour_xs = []
        tour_ys = []
        j = 0
        while j < len(tour):
            tour_xs.append(xs[tour[j]])
            tour_ys.append(ys[tour[j]])
            j += 1
        tour_xs.append(xs[tour[0]])
        tour_ys.append(ys[tour[0]])

        ax.plot(tour_xs, tour_ys, "b-")
        ax.scatter(xs, ys, color="red", zorder=5)

        k = 0
        while k < len(coords):
            ax.annotate(str(k), (xs[k] + 1, ys[k] + 1))
            k += 1

        ax.set_title("Generacja {}".format(gen + 1))
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.grid(True)

    anim = FuncAnimation(fig, update, frames=len(history), interval=200, repeat=False)
    show()
