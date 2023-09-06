with open('../data/05.txt') as file:
    input = file.read().strip().split('\n')

input = [int(ins) for ins in input]

def part1():
    steps = 0
    i = 0
    while True:
        try:
            tmp = input[i]
            input[i] += 1
            i += tmp
            steps += 1
        except IndexError:
            break

    print(steps)

def part2():
    steps = 0
    i = 0
    while True:
        try:
            tmp = input[i]
            if tmp >= 3:
                input[i] -= 1
            else:
                input[i] += 1
            i += tmp
            steps += 1
        except IndexError:
            break

    print(steps)


#--- run part 2 after running part 1 ---#

#part1()
part2()