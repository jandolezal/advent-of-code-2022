
"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""


def part1(data, chars=4):
    for i in range(0, len(data)):
        if len(set(data[i: i+chars])) == chars:
            return i + chars


# Part 1
test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_result = part1(test_data)
assert test_result == 7, f'Part 1 should be 7, but is {test_result}'

with open('06/input.txt') as f:
    data = f.read()

result1 = part1(data)
print(result1)

# Part 2
test_result2 = part1(test_data, chars=14)
assert test_result2 == 19, f'Part 1 should be 7, but is {test_result2}'
result2 = part1(data, chars=14)
print(result2)
