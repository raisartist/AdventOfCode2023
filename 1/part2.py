import re

data = open('input.txt', 'r').read().split('\n')
dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9 
}

answer = 0

for input in data:

    found = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))', input)
    if len(found) > 0:
        calibration = ""
        first = found[0]
        last = found[-1]

        if first in dict:
            calibration += str(dict[first])
        else:
            calibration += str(first)

        if last in dict:
            calibration += str(dict[last])
        else:
            calibration += str(last)

        answer += int(calibration)

print(answer)