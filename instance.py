import numpy as np
from config import NUM_CITIES, DISTANCE_MIN, DISTANCE_MAX

table = []

def make_table(seed_num):
    global table
    
    rng = np.random.default_rng(seed_num)
    
    n = NUM_CITIES
    table = np.zeros((n, n), dtype=int)
    i = 0
    while i < n:
        j = 0
        while j < n:
            number = rng.integers(DISTANCE_MIN, DISTANCE_MAX + 1)
            if i != j:
                table[i][j] = number
            j += 1
        i += 1

def read_file(file_path):
    global table
    table = np.loadtxt(file_path, delimiter=",", dtype=int)