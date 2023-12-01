import re

data = open('input.txt', 'r').read().split('\n')
sum = 0

for input in data:
    calibrationList = re.findall(r'[0-9]', input)
    if len(calibrationList) > 0:
        calibration = str(calibrationList[0]) + str(calibrationList[-1])
        sum += int(calibration)

print(f" answer: {sum}")