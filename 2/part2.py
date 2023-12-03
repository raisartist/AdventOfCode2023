from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

answer = 0

for input in data:

    split_input = input.split(':')
    curr_id = int(split_input[0].split(' ')[1])

    draws = [[y.split(' ') for y in x.split(',')] for x in split_input[1].split(';')]

    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for draw in draws:
        for cube in draw:
            value = int(cube[1])
            dict_value = min_cubes[cube[2]]
            min_cubes[cube[2]] = max(value, dict_value)

    power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
    answer += power


print(answer)
