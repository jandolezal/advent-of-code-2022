'''
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
'''


def load_data(filename):
    with open(filename) as f:
        lines = [line.strip('\n') for line in f.readlines()]
        data = [tuple(line.split(' ')) for line in lines]
    return data


def part1(data):
    points_map = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

    scores = []

    for row in data:
        points = points_map[row[1]]
        # draw
        if row in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]:
            score = 3 + points
        # win
        elif row in [('A', 'Y'), ('B', 'Z'), ('C', 'X')]:
            score = 6 + points
        # lose
        else:
            score = 0 + points
        scores.append(score)
    
    return sum(scores)


def part2(data):
    points_map = {'A': 1, 'B': 2, 'C': 3}

    win = {'A': 'B', 'B': 'C', 'C': 'A'}
    lose = {v: k for k, v in win.items()}

    scores = []

    for action, outcome in data:
        # lose
        if outcome == 'X':
            reaction = lose[action]
            score = 0 + points_map[reaction]
        # draw
        elif outcome == 'Y':
            score = 3 + points_map[action]
        # win
        else:
            reaction = win[action]
            score = 6 + points_map[reaction]
        scores.append(score)

    return sum(scores)


test_data = load_data('02/test_input.txt')
print(test_data)
data = load_data('02/input.txt')

# Part 1
assert part1(test_data) == 15, 'Part 1 is wrong'
result1 = part1(data)
print(result1)

# Part 2

assert part2(test_data) == 12, 'Part 2 is wrong'
result2 = part2(data)
print(result2)

