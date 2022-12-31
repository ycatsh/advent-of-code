with open('input.txt') as file:
    inputs = []
    for i in file.read().strip().split('\n'):
        inputs.append(i)

chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


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
