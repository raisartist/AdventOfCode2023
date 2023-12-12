from os.path import dirname, join
from collections import defaultdict
import numpy as np
import re

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

instructions = data[0]*5000
nodes = defaultdict(dict)

directions = np.array(data)
directions = directions[2:669]

for line in directions:

    split_direction = line.split()
    key = split_direction[0]
    left = re.sub('[^a-zA-Z]+', '', split_direction[2])
    right = re.sub('[^a-zA-Z]+', '', split_direction[3])

    nodes[key]["L"] = left
    nodes[key]["R"] = right

node_keys = nodes.keys()
def filter_func(variable):
    if variable[-1] == "A":
        return True
    else:
        return False
    
filtered_node_keys = list(filter(filter_func, node_keys))

answer = []
for key in filtered_node_keys:
    current_node = key
    steps = 0

    for instruction in instructions:
        if current_node[-1] == "Z":
            print("Found ZZZ!")
            break
        else:
            # print(f"current node:{current_node}")
            # print(f"next turn: {instruction}")
            next_node = nodes[current_node][instruction]
            current_node = next_node
            steps +=1
            # print(f"new node: {current_node}")
    answer.append(steps)
print(answer)

#I took the array of individual paths and calculated LCM via Excel


