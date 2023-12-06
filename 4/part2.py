from os.path import dirname, join
import re
from collections import defaultdict

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read().split('\n')

copies = defaultdict(int)

for card_idx, card in enumerate(data):
    card_number = card_idx + 1
    copies[card_number] += 1

    matches = 0

    card_split = card.split(':')[1]
    win_cards_string = card_split.split('|')[0]
    actual_cards_string = card_split.split('|')[1]

    win_cards = re.findall(r'[0-9][0-9]|[0-9]', win_cards_string)
    actual_cards = re.findall(r'[0-9][0-9]|[0-9]', actual_cards_string)

    for number in actual_cards:
        if number in win_cards:
            matches +=1
    for j in range(copies[card_number]):
        for i in range(matches):
            copies[card_number+(i+1)] += 1

print(sum(copies.values()))
