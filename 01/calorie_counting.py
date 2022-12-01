'''
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
'''

def load_data(filename):
    with open(filename) as f:
        data = []
        elf = []
        for line in f.readlines():
            if line == '\n':
                data.append(elf)
                elf = []
            else:
                elf.append(int(line.strip('\n')))
        return data


def part1(data):
    sums = [sum(elf) for elf in data]
    return max(sums)


# Part 1
test_data = load_data('01/test_input.txt')
print(test_data)
test_result = part1(test_data)
assert test_result == 24000, 'Part 1 is wrong.'
print(test_result)

data = load_data('01/input.txt')
result = part1(data)
print(result)
