'''
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8
'''


def load_data(filepath):
    with open(filepath) as f:
        return [[int(char) for char in line] for line in f.read().split()]



def part1(data):
    count = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            this = data[i][j]

            right = all(num < this for num in data[i][j+1:])
            left = all(num < this for num in data[i][:j])
            top = all(num < this for num in [num[j] for num in data[:i]])
            down = all(num < this for num in [num[j] for num in data[i+1:]])

            if top or right or down or left:
                count += 1
    
    return count


def part2(data):
    scores = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            this = data[i][j]

            left = [num >= this for num in reversed(data[i][:j])]
            right = [num >= this for num in data[i][j+1:]]
            top = [num >= this for num in reversed([row[j] for row in data[:i]])]
            down = [num >= this for num in [row[j] for row in data[i+1:]]]
            
            tree_count = 1

            for direction in [left, right, top, down]:
                if len(direction) == 0:
                    tree_count = 0
                    break
                try: 
                    tree_count = tree_count * (direction.index(True) + 1)
                except ValueError:
                    tree_count = tree_count * len(direction)

            scores.append(tree_count)

    return max(scores)


test_data = load_data('08/test_input.txt')
data = load_data('08/input.txt')

# Part 1
test_result = part1(test_data)
assert test_result == 21, f'Part 1 should be 21, but is {test_result}'
result1 = part1(data)
print(result1)


# Part 2
test_result2 = part2(test_data)
assert test_result2 == 8, f'Part 1 should be 8, but is {test_result2}'
result2 = part2(data)
print(result2)
