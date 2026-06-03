import numpy as np
from config import NUM_CITIES

table = []
coords = []

def make_table(rng):
    global table, coords

    n = NUM_CITIES
    coords = rng.integers(0, 100, size=(n, 2)).tolist()

    table = np.zeros((n, n), dtype=int)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i != j:
                dx = coords[i][0] - coords[j][0]
                dy = coords[i][1] - coords[j][1]
                table[i][j] = int(np.sqrt(dx * dx + dy * dy))
            j += 1
        i += 1

def read_file(file_path):
    global table
    table = np.loadtxt(file_path, delimiter=",", dtype=int)
