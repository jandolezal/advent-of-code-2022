'''
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3
'''

import string


low = {char: priority+1 for priority, char in enumerate(string.ascii_lowercase)}
upp = {char: priority+27 for priority, char in enumerate(string.ascii_uppercase)}
PRIORITIES = {**low, **upp}


def load_data(filename):
    with open(filename) as f:
        data = f.read().split()
    return data


def part1(data, priorities):

    # Split lines to rucksack compartments
    rucksacks = []
    
    for line in data:
        i = int(len(line)/2)
        rucksacks.append((line[:i], line[i:]))

    # Find chars
    chars = []

    for first, second in rucksacks:
        char = list(set(first) & set(second))[0]
        chars.append(char)
    
    # Assign scores
    scores = [priorities[char] for char in chars]

    return sum(scores)


def part2(data, priorities):
    scores = []

    rucksacks = []
    group = []

    # Gather rucksacks for groups as three sets in a list
    for i, line in enumerate(data):
        if (i % 3 == 0):
            group = []
            rucksacks.append(group)
        group.append(set(line))

    # Find badges within groups and assign scores
    chars = [list(set.intersection(*group))[0] for group in rucksacks]
    scores = [priorities[char] for char in chars]

    return sum(scores)



test_data = load_data('03/test_input.txt')
print(test_data)

data = load_data('03/input.txt')


# Part 1
assert part1(test_data, PRIORITIES) == 157, 'The sum of scores should be 157'
result1 = part1(data, PRIORITIES)
print(result1)


# Part 2
assert part2(test_data, PRIORITIES) == 70, 'The sum of scores should be 70'
result2 = part2(data, PRIORITIES)
print(result2)
