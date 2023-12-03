from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

answer = 0

for input in data:

    split_input = input.split(':')
    curr_id = int(split_input[0].split(' ')[1])

    draws = [[y.split(' ') for y in x.split(',')] for x in split_input[1].split(';')]

    valid_draw = True

    for draw in draws:
        valid_cube = True
        for cube in draw:
            value = int(cube[1])
            max = limit[cube[2]]
            if value > max:
                valid_cube = False
        if valid_cube == False:
            valid_draw = False

    if valid_draw == True:
        answer += curr_id

print(answer)
