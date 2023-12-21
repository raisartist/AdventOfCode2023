from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')
data_matrix = []
for line in data:
    data_matrix.append([[*char]for char in line])

def expand():
    empty_rows = []
    empty_columns = []
    for h_index, height in enumerate(data_matrix):
        if all(item == ["."] for item in height):
            print(f"adding empty row {h_index}")
            empty_rows.append(h_index)
    for w_index, width in enumerate(data_matrix[0]):
        if all(item[w_index] == ["."] for item in data_matrix):
            print(f"adding empty column {w_index}")
            empty_columns.append(w_index)

    return empty_rows, empty_columns
            
def find_galaxies(empty_rows, empty_columns, expansion):
    galaxies = []
    extra_rows = 0
    for l_idx, line in enumerate(data_matrix):
        if l_idx in empty_rows:
            extra_rows+=expansion
        extra_columns = 0
        for c_idx, char in enumerate(line):
            if c_idx in empty_columns:
                extra_columns+=expansion
            if char == ['#']:
                galaxies.append([l_idx + extra_rows, c_idx+extra_columns])
    return galaxies

def find_paths(galaxies):
    path_sum = 0
    for g_idx, galaxy in enumerate(galaxies):
        gals_to_check = galaxies[g_idx+1:]
        for sh_idx, sh_gal in enumerate(gals_to_check):
            path = abs(sh_gal[1] - galaxy[1])+abs(sh_gal[0]-galaxy[0])
            path_sum+=path
    return path_sum


print("starting:")
empty_rows, empty_columns = expand()
print("expanded")
galaxies = find_galaxies(empty_rows, empty_columns, 999999)
print('found galaxies')
answer = find_paths(galaxies)
print(answer)

