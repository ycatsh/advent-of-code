with open('../data/01.txt') as file:
    input = file.read().strip()

def part1():
    digits = []
    for i in range(len(input)):
        if input[i] == input[(i+1)-len(input) if i+1 >= len(input) else i+1]:
            digits.append(int(input[i]))    
    
    print(sum(digits))

def part2():
    digits = []
    for i in range(len(input)):
        if input[i] == input[int((i+(len(input)/2))-len(input) if i+(len(input)/2) >= len(input) else i+(len(input)/2))]:
            digits.append(int(input[i]))

    print(sum(digits))

part1() # part 1 
part2() # part 2
