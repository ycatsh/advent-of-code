with open('../Data/d1.txt') as file:
    inputs = file.read().strip().split(', ')

directions = {'R': 1, 'L':-1}
rotations = {0: [0,1j], 1: [1,0], 2: [0,-1j], 3: [-1,0]}
rotation = 0

def part1(data, d, rs, r):
    path = [0,0]

    for i in data:
        blocks = int(i[1:])
        r = (r + d[i[0]])%4

        for _ in range(blocks):
            path[0] += rs[r][0]
            path[1] += rs[r][1]

    print(abs(path[0])+abs(path[1]))


def part2(data, d, rs, r):
    visited = [[0,0],]
    path = [0,0]

    for i in data:
        blocks = int(i[1:])
        r = (r + d[i[0]])%4

        for _ in range(blocks):
            path[0] += rs[r][0]
            path[1] += rs[r][1]

            if [path[0], path[1]] in visited:
                print(abs(path[0])+abs(path[1]))
                return
            else:
                visited.append([path[0], path[1]])


part1(inputs, directions, rotations, rotation) # part 1
part2(inputs, directions, rotations, rotation) # part 2