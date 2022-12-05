'''
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5
'''

import queue
from collections import defaultdict


def clean_instruction(instruction):
    return [int(element) for element in instruction.split(' ') if element.isdigit()]


def load_data(filepath):
    with open(filepath) as f:
        lines = f.readlines()

        i = lines.index('\n')
        raw_crates = lines[:i-1]
        raw_instructions = lines[i+1:]

        crate_rows = [list(enumerate(row[1::4], start=1)) for row in raw_crates[::-1]]

        stacks = defaultdict(queue.LifoQueue)
        for row in crate_rows:
            for stack,label in row:
                if label != ' ':
                    stacks[stack].put(label)

        instructions = [clean_instruction(inst.strip()) for inst in raw_instructions]

    return stacks, instructions


def part1(stacks, instructions):
    
    for (count, _from, to) in instructions:
        for _ in range(count):
            item = stacks[_from].get()
            stacks[to].put(item)
    
    top_crates = ''.join([stacks[k].get() for k in stacks.keys()])
    
    return top_crates


def part2(stacks, instructions):
    
    for (count, _from, to) in instructions:
        items = [stacks[_from].get() for _ in range(count)]

        for item in items[::-1]:
            stacks[to].put(item)
    
    top_crates = ''.join([stacks[k].get() for k in stacks.keys()])
    
    return top_crates

# Part 1
test_stacks, test_instructions = load_data('05/test_input.txt')
stacks, instructions = load_data('05/input.txt')

assert part1(test_stacks, test_instructions) == 'CMZ'

result1 = part1(stacks, instructions)
print(result1)


# Part 2
test_stacks, test_instructions = load_data('05/test_input.txt')
stacks, instructions = load_data('05/input.txt')

assert part2(test_stacks, test_instructions) == 'MCD'

result2 = part2(stacks, instructions)
print(result2)
