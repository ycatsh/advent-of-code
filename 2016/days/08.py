import numpy

with open('../data/08.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

display = numpy.zeros((50,6), dtype=numpy.int_)

for ins in range(len(inputs)):
    if ins[0] == 'rect':
        for i in range(int(ins[2])):
            for j in range(int(ins[4])):
                display[i][j] == 1

    if ins[:3] == 'rotate row':
        for j in range(int(ins[4])):
            pass 
    if ins[:3] == 'rotate column':
        pass
