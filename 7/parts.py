import collections
from os.path import dirname, join
import numpy as np

current_dir = dirname(__file__)
file_path = join(current_dir, "input.txt")
data = open(file_path, 'r').read()

CARDS1 = "AKQJT98765432"
CARDS2 = "AKQT98765432J"

def measure1(card):
    counts = [v for k, v in collections.Counter(card).most_common()]
    return counts + [-CARDS1.index(c) for c in card]

def measure2(card):
    counter = collections.Counter(card)
    counts = [v for k, v in counter.most_common()]
    jokers = counter["J"]
    if jokers > 0 and jokers < 5:
        if counts[0] == jokers:
            counts[0] = counts[0] + counts[1]
            counts.remove(counts[1])
        elif jokers < counts[0]:
            counts[0] += jokers
            counts.remove(jokers)
    return counts + [-CARDS2.index(c) for c in card]

# print(measure2("29QA4"))

def part1(text):
    hands = [line.split() for line in text.strip().split("\n")]

    hands.sort(key=lambda h: measure1(h[0]))
    return sum(i * int(bid) for i, (cards, bid) in enumerate(hands, 1))

def part2(text):
    hands = [line.split() for line in text.strip().split("\n")]

    hands.sort(key=lambda h: measure2(h[0]))
    return sum(i * int(bid) for i, (cards, bid) in enumerate(hands, 1))

print(part2(data))
