with open('../data/02.txt') as file:
    input = file.read().strip().split('\n')

def part1():
    diffs = 0
    for line in input:
        row = line.split('\t')
        row = [int(n) for n in row]
        diffs += (max(row)-min(row))

    print(diffs)

def part2():
    divs = 0
    for line in input: 
        row = line.split('\t')
        row = [int(n) for n in row]

        for i in row:
            for j in row:
                if i != j:
                    if i % j == 0:
                        divs += (i/j)
    print(divs)

part1() # part 1
part2() # part 2
