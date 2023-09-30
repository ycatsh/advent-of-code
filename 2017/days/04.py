with open('../data/04.txt') as file:
    input = file.read().strip().split('\n')

def part1():
    valid = 0
    for line in input:
        line = line.split(' ')
        if len(set(line)) == len(line):
            valid += 1

    print(valid)

def part2():
    valid = 0 
    for line in input:
        line = line.split(' ')
        line = [sorted(element) for element in line]
        sorted_pwd = ''
        sorted_line = []
        for chars in line:
            for char in chars:
                sorted_pwd += char
            sorted_line.append(sorted_pwd)
            sorted_pwd = ''

        if len(set(sorted_line)) == len(sorted_line):
            valid += 1

    print(valid)

part1() # part 1 
part2() # part 2
