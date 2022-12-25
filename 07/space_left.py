"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""


def load_data(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()]


def make_tree(data):
    tree = {}
    cwd = ('/',)
    tree[cwd] = 0

    for line in data:
        if line == '$ cd /':
            cwd = ('/',)
        elif line == '$ cd ..':
            if cwd == ('/',):
                continue
            else:
                cwd = cwd[:-1]
        elif line.startswith('$ cd'):
            dirname = line.split(' ')[-1]
            cwd = cwd + (dirname,)
            tree.setdefault(cwd, 0)
        elif line == '$ ls' or line == '' or line.startswith('dir'):
            continue
        else: # line with a file
            first, second = line.split(' ')
            path = cwd + (second,)
            tree[path] = int(first)
    return tree


def part1(tree):
    counts = {}
    for path, size in tree.items():
        while path:
            path = path[:-1]
            if path:
                counts.setdefault(path, 0)
                counts[path] += size
    return sum(v for v in counts.values() if v <= 100_000)


def part2(tree):
    counts = {}
    for path, size in tree.items():
        while path:
            path = path[:-1]
            if path:
                counts.setdefault(path, 0)
                counts[path] += size

    needed_space = 30_000_000 - (70_000_000 - counts[('/',)])
    candidates = [v for v in counts.values() if v >= needed_space]

    return min(candidates)


test_data = load_data('07/test_input.txt')
test_tree = make_tree(test_data)
data = load_data('07/input.txt')
tree = make_tree(data)

# Part 1
test_counts = part1(test_tree)
assert test_counts == 95437, 'Part 1 should be 95437'
counts = part1(tree)
print(counts)

# Part 2
test_size = part2(test_tree)
assert test_size == 24933642, 'Part 2 should be 24933642'
size = part2(tree)
print(size)
