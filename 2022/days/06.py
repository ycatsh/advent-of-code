with open('../data/06.txt') as file:
    inputs = file.read()

def part1():
    for i in range(len(inputs)-4):
        # print(set(inputs[i:i+4]))
        if len((set(inputs[i:i+4]))) == 4:
            print(i+4)
            break

def part2():
    for j in range(len(inputs)-14):
        if len((set(inputs[j:j+14]))) == 14:
            print(j+14)
            break

part1() # part 1
part2() # part 2
