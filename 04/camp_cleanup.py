'''
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
'''


def load_data(filename):
    with open(filename) as f:
        lines = f.read().split()
        data = []
        for line in lines:
            first, second = line.split(',')
            first = tuple(int(num) for num in first.split('-'))
            second = tuple(int(num) for num in second.split('-'))
            data.append([first, second])
    return data


def part1(data):
    count = 0

    for (f_min, f_max), (s_min, s_max) in data:
        first_is_included = f_min >= s_min and f_max <= s_max
        second_is_includec = f_min <= s_min and f_max >= s_max

        if first_is_included or second_is_includec:
            count += 1

    return count


def part2(data):
    count = 0

    for (f_min, f_max), (s_min, s_max) in data:
        first_is_first = f_min < s_min and f_max < s_min
        second_is_first = f_min > s_min and f_min > s_max

        if not (first_is_first or second_is_first):
            count += 1

    return count



test_data = load_data('04/test_input.txt')
print(test_data)
data = load_data('04/input.txt')


# Part 1
assert part1(test_data) == 2, 'Part 1 should be 2.'
result1 = part1(data)
print(result1)

# Part 2
assert part2(test_data) == 4, 'Part 2 should be 4.'
result2 = part2(data)
print(result2)
