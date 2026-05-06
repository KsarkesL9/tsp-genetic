import sys
import instance
from config import SEED
from ga import start, count_distance
from plots import draw_chart

def main():
    seed_num = SEED
    file_to_load = ""
    is_loading = False
    
    try:
        if len(sys.argv) > 1:
            seed_num = int(sys.argv[1])
        if len(sys.argv) > 2:
            file_to_load = sys.argv[2]
            is_loading = True
    except Exception:
        print("Cos poszlo nie tak")
        pass

    if is_loading == True:
        instance.read_file(file_to_load)
    else:
        instance.make_table(seed_num)
        
    table = instance.table

    print("Liczba miast: {}".format(len(table)))
    print("Ziarno: {}".format(seed_num))

    my_ga = start(table, seed_num)

    result = my_ga.best_solution()
    best_answer = result[0]
    
    length = count_distance(best_answer, table)

    answer_numbers = []
    i = 0
    while i < len(best_answer):
        answer_numbers.append(int(best_answer[i]))
        i += 1

    print("Najlepsza trasa: {}".format(str(answer_numbers)))
    print("Dlugosc trasy: {}".format(int(length)))

    draw_chart(my_ga)

if __name__ == "__main__":
    main()