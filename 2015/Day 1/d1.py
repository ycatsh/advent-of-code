with open('input.txt') as file:
    inputs = []
    for i in file.read():
        inputs.append(i)


def part1(data):
    floor = 0

    for j in data:
        if j == '(':
            floor += 1
        if j == ')':
            floor -= 1

    print(floor)


def part2(data):
    floor = 0
    pointer = 0

    for j in data:
        if floor < 0:
            break
        if j == '(':
            floor += 1
        if j == ')':
            floor -= 1
        pointer += 1

    print(pointer)

part1(inputs) # part 1
part2(inputs) # part 2
