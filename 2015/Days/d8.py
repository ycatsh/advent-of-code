with open ('../Data/d8.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

char = sum([len(i) for i in inputs])

def part1(data, num):
    memory = 0

    for word in data:
        memory += len(eval(word))

    print(num-memory)


def part2(data, num):
    encoded = 0 

    #not done

part1(inputs, char) # part 1
#part2(inputs, char) # part 2