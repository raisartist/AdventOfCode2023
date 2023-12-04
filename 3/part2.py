from os.path import dirname, join
from collections import defaultdict

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

def isChar(char):
    # print(f"checking {char}")
    if char == "*":
        return True

# print([*data[0]])
test_input = [data[0]]
# print(f"test_input: {test_input}")

numbers = defaultdict(list)
dict_key = ''

numbers_with_two = []

for line_idx, line_val in enumerate(data):
    print(f"LINE: {line_idx}")
    number = ''
    is_valid_number = False
    for char_idx, char_val in enumerate(line_val):
        if char_val.isdigit():
            number += char_val
            left = line_val[char_idx - 1]
            right = line_val[char_idx + 1]
            top = data[line_idx - 1][char_idx]
            bottom = data[line_idx + 1][char_idx]
            top_left = data[line_idx - 1][char_idx - 1]
            top_right = data[line_idx - 1][char_idx + 1] 
            bottom_left = data[line_idx + 1][char_idx - 1] 
            bottom_right = data[line_idx + 1][char_idx + 1] 

            if isChar(left):
                dict_key = str(str(line_idx)+"-"+str(char_idx - 1))
                is_valid_number = True
            elif isChar(right):
                dict_key = str(str(line_idx)+"-"+str(char_idx + 1))
                is_valid_number = True
            elif isChar(top):
                dict_key = str(str(line_idx - 1)+"-"+str(char_idx))
                is_valid_number = True
            elif isChar(bottom):
                dict_key = str(str(line_idx + 1)+"-"+str(char_idx))
                is_valid_number = True
            elif isChar(top_left):
                dict_key = str(str(line_idx - 1)+"-"+str(char_idx - 1))
                is_valid_number = True
            elif isChar(top_right):
                dict_key = str(str(line_idx - 1)+"-"+str(char_idx + 1))
                is_valid_number = True
            elif isChar(bottom_left):
                dict_key = str(str(line_idx + 1)+"-"+str(char_idx - 1))
                is_valid_number = True
            elif isChar(bottom_right):
                dict_key = str(str(line_idx + 1)+"-"+str(char_idx + 1))
                is_valid_number = True
        else:
            if is_valid_number:
                numbers[dict_key].append(number)
                number = ''
                is_valid_number = False
            else:
                number = ''

print(numbers)

for key,value in numbers.items():
    if len(value) == 2:
        numbers_with_two.append(int(value[0]) * int(value[1]))

print(sum(numbers_with_two))
        
              