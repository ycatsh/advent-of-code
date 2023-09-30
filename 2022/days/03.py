import string

with open('../data/03.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

chars = [_ for _ in string.ascii_letters]

def part1(chars):
    items = 0

    for j in inputs:
        half = int(len(j)/2)

        first = set(j[:half])
        second = set(j[half:])

        for k in chars:
            if k in first and k in second:
                items += (chars.index(k)+1)

    print(items)

def part2(chars):
    next = 3
    length = len(inputs)
    items = 0

    for j in range(0, length, 3):
        comp = inputs[j:next]
        next += 3

        for k in chars:
            if k in comp[0] and k in comp[1] and k in comp[2]:
                items += (chars.index(k)+1)

    print(items)

part1(chars) # part 1
part2(chars) # part 2
