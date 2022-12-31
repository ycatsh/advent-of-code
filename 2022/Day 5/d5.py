with open('input.txt') as file:
    inputs = []
    for i in file.read().strip().split('\n\n'):
        inputs.append(i.splitlines())

# as you can tell, I was stuck.
stacks1 = {1: ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
           2: ['Q', 'R', 'B'],
           3: ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
           4: ['D', 'V', 'F', 'R', 'Q', 'H'],
           5: ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
           6: ['W', 'R', 'T', 'Z'],
           7: ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
           8: ['R', 'N', 'F', 'H', 'W'],
           9: ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']}

stacks2 = {1: ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
           2: ['Q', 'R', 'B'],
           3: ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
           4: ['D', 'V', 'F', 'R', 'Q', 'H'],
           5: ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
           6: ['W', 'R', 'T', 'Z'],
           7: ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
           8: ['R', 'N', 'F', 'H', 'W'],
           9: ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']}


def part1(data):
    for moves in data[1]:
        move = moves.split(' ')

        for j in range(int(move[1])):
            rmStacks = stacks1[int(move[3])].pop()
            stacks1[int(move[5])].append(rmStacks)

    stackEnds = ''
    for k in stacks1:
        stackEnds += stacks1[k][-1]

    print(f'part 1: {stackEnds}')  # part 1


def part2(data):
    for moves in data[1]:
        move = moves.split(' ')

        rmStacks = stacks2[int(move[3])][-int(move[1]):]
        stacks2[int(move[3])] = stacks2[int(move[3])][:-int(move[1])]

        for j in rmStacks:
            stacks2[int(move[5])].append(j)

    stackEnds = ''
    for k in stacks2:
        stackEnds += stacks2[k][-1]

    print(f'part 2: {stackEnds}')  # part 2


part1(inputs)
part2(inputs)
