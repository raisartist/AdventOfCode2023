from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

def isChar(char):
    # print(f"checking {char}")
    if char.isalnum() == False and char != ".":
        return True

# print([*data[0]])
test_input = [data[0]]
# print(f"test_input: {test_input}")

answer = 0

for line_idx, line_val in enumerate(data):
    print(f"LINE: {line_idx}")
    number = ''
    is_valid_number = False
    for char_idx, char_val in enumerate(line_val):
        if char_val.isdigit():
            print(f"adding {char_val} to {number}")
            number += char_val
            try:
                left = line_val[char_idx - 1]
            except:
                left = '.'
            try:
                right = line_val[char_idx + 1]
            except:
                right = '.'
            try:
                top = data[line_idx - 1][char_idx]
            except:
                top = '.'
            try:
                bottom = data[line_idx + 1][char_idx]
            except:
                bottom = '.'
            try:
                top_left = data[line_idx - 1][char_idx - 1]
            except: top_left = '.'
            try:
                top_right = data[line_idx - 1][char_idx + 1] 
            except:
                top_right = '.'
            try:
                bottom_left = data[line_idx + 1][char_idx - 1] 
            except:
                bottom_left = '.'
            try:
                bottom_right = data[line_idx + 1][char_idx + 1] 
            except: 
                    bottom_right = '.'
            if isChar(left) or isChar(right) or isChar(top) or isChar(bottom) or isChar(top_left) or isChar(top_right) or isChar(bottom_left) or isChar(bottom_right):
                print(f"{char_val} is adjacent")
                is_valid_number = True
            # else:
                # print(f"{char_val} is not adjacent")
        else:
            if is_valid_number:
                print(f"adding {number} to the answer")
                answer += int(number)
                number = ''
                is_valid_number = False
            else:
                number = ''

print(answer)
        
              