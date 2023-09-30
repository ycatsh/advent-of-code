import numpy

with open ('../data/06.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

display = numpy.zeros((1000,1000), dtype=numpy.int_)
#0: off, 1: on

def part1(data, screen):
    for line in range(len(data)):
        cmd = inputs[line].split(' ')
        
        if cmd[0] == 'toggle':
            x, y = cmd[1].split(',')
            x2, y2 = cmd[3].split(',')
            
            for i in range(int(x), int(x2)+1):
                for j in range(int(y), int(y2)+1):
                    screen[i][j] = 1 - screen[i][j]

        if cmd[1] == 'off':
            x, y = cmd[2].split(',')
            x2, y2 = cmd[4].split(',')

            for i in range(int(x), int(x2)+1):
                for j in range(int(y), int(y2)+1):
                    screen[i][j] = 0

        if cmd[1] == 'on':
            x, y = cmd[2].split(',')
            x2, y2 = cmd[4].split(',')

            for i in range(int(x), int(x2)+1):
                for j in range(int(y), int(y2)+1):
                    screen[i][j] = 1

    print(sum(sum(lit) for lit in screen))

def part2(data, screen):
    for line in range(len(data)):
        cmd = inputs[line].split(' ')
        
        if cmd[0] == 'toggle':
            x, y = cmd[1].split(',')
            x2, y2 = cmd[3].split(',')
            
            for i in range(int(x), int(x2)+1):
                for j in range(int(y), int(y2)+1):
                    screen[i][j] += 2

        if cmd[1] == 'off':
            x, y = cmd[2].split(',')
            x2, y2 = cmd[4].split(',')

            for i in range(int(x), int(x2)+1):
                for j in range(int(y), int(y2)+1):
                    if not screen[i][j] == 0:
                        screen[i][j] -= 1

        if cmd[1] == 'on':
            x, y = cmd[2].split(',')
            x2, y2 = cmd[4].split(',')

            for i in range(int(x), int(x2)+1):
                for j in range(int(y), int(y2)+1):
                    screen[i][j] += 1

    print(sum(sum(bright) for bright in screen))


#--- call part 2 after running part 1 ---#
part1(inputs, display) # part 1
#part2(inputs, display) # part 2 
