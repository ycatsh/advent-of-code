with open('../data/03.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]


def part1(data):
    valid = 0

    for i in range(len(data)):
        j = data[i].split(' ')
        sides = sorted(list(map(int, [k for k in j if k.strip()])))

        if sides[0] + sides[1] > sides[2]:
            valid += 1 
    
    print(valid)


def part2(data):
    sides = []
    valid = 0

    for i in range(len(data)):
        j = data[i].split(' ')
        tmp = list(map(int, [k for k in j if k.strip()]))
        sides.append(tmp)

    s1, s2, s3 = [i[0] for i in sides], [i[1] for i in sides], [i[2] for i in sides]
    sides_col = s1+s2+s3

    while sides_col: 
        sides_f = sorted([sides_col[0], sides_col[1], sides_col[2]])
        if sides_f[0] + sides_f[1] > sides_f[2]:
            valid += 1

        sides_col = sides_col[3:] 

    print(valid)

part1(inputs) # part 1
part2(inputs) # part 2
