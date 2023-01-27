import string

with open('../Data/d3.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

chars = [i for i in string.ascii_letters]

def part1(charsList):
    sumItems = 0

    for j in inputs:
        half = int(len(j)/2)

        firstComp = set(j[:half])
        secondComp = set(j[half:])

        for k in charsList:
            if k in firstComp and k in secondComp:
                sumItems += (charsList.index(k)+1)

    print(f'part 1: {sumItems}')


def part2(charList):
    nextGroup = 3
    length = len(inputs)
    sumItems = 0

    for j in range(0, length, 3):
        comp = inputs[j:nextGroup]
        nextGroup += 3

        for k in charList:
            if k in comp[0] and k in comp[1] and k in comp[2]:
                sumItems += (charList.index(k)+1)

    print(f'part 2: {sumItems}')


part1(chars)
part2(chars)
