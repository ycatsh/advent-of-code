with open('../data/05.txt') as file:
    inputs = [i.splitlines() for i in file.read().strip().split('\n\n')]

# as you can tell, I was stuck.
stacks = {1: ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
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

        for _ in range(int(move[1])):
            rm_stacks = stacks[int(move[3])].pop()
            stacks[int(move[5])].append(rm_stacks)

    stack_ends = ''
    for k in stacks:
        stack_ends += stacks[k][-1]

    print(stack_ends)

def part2(data):
    for moves in data[1]:
        move = moves.split(' ')

        rm_stacks = stacks[int(move[3])][-int(move[1]):]
        stacks[int(move[3])] = stacks[int(move[3])][:-int(move[1])]

        for j in rm_stacks:
            stacks[int(move[5])].append(j)

    stack_ends = ''
    for k in stacks:
        stack_ends += stacks[k][-1]

    print(stack_ends)


#--- run part 2 after running part 1 ---#
part1(inputs) # part 1
#part2(inputs) # part 2
