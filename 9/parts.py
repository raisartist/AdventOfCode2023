from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')
readings = [line.split(' ') for line in data]

def solution1():
    answers = []
    for reading in readings:
        reading = [int(item) for item in reading]
        print(reading)
        prediction = 0
        reductions = [reading]
        while set(reductions[-1]) != {0}:
            # print(f"arr in while: {arr}")
            diff_arr = []
            for number in range(len(reductions[-1])-1):
                diff = int(reductions[-1][number+1])-int(reductions[-1][number])
                diff_arr.append(diff)
            # print(f"diff_arr: {diff_arr}")
            reductions.append(diff_arr)
        print(f"sol 1 reductions:: {reductions}")
        last_nums = [i[-1] for i in reductions]
        print(f"last nums: {last_nums}")
        prediction = sum(last_nums)
        print(f"prediction: {prediction}")
        answers.append(prediction)
    print(sum(answers))

# solution1()

def part2():
    answers = []
    for reading in readings:
        reading = [int(item) for item in reading]
        predictions = [0]
        reductions = [reading]
        while set(reductions[-1]) != {0}:
            # print(f"arr in while: {arr}")
            diff_arr = []
            for number in range(len(reductions[-1])-1):
                diff = int(reductions[-1][number+1])-int(reductions[-1][number])
                diff_arr.append(diff)
            # print(f"diff_arr: {diff_arr}")
            reductions.append(diff_arr)
        # print(f"part 2 reductions:: {reductions}")
        
        while len(predictions) != len(reductions):
            for line in range(len(reductions)-2, -1, -1):
                # print(f"comparing{reductions[line][0]} with {predictions[-1]}")
                new_prediction = reductions[line][0] - predictions[-1]
                predictions.append(new_prediction)
        # print(f"predictions: {predictions}")
        answers.append(predictions[-1])
    print(sum(answers))

part2()




