from os.path import dirname, join
import re

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

answer = 0

for pile in data:
    points = 0
    matches = 0

    card_split = pile.split(':')[1]
    win_cards_string = card_split.split('|')[0]
    actual_cards_string = card_split.split('|')[1]

    win_cards = re.findall(r'[0-9][0-9]|[0-9]', win_cards_string)
    actual_cards = re.findall(r'[0-9][0-9]|[0-9]', actual_cards_string)

    for card in actual_cards:
        if card in win_cards:
            matches +=1
    if matches > 1:
        points = 2**(matches-1)
    elif matches == 1:
        points = 1
    else:
        points = 0
    
    answer +=points

print(answer)
