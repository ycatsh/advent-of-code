with open('input.txt') as file:
    inputs = []
    for i in file.read().strip().split('\n'):
        inputs.append(i)

def part1(data):
    total_area = 0 

    for j in data:
        dim = list(map(int, j.split('x')))
        arr = list((dim[0]*dim[1], dim[1]*dim[2], dim[2]*dim[0]))

        area = 2*(sum(arr))
        slag = min(arr)

        total_area += area+slag

    print(total_area)

def part2(data):
    total_feet = 0

    for j in data:
        dim = list(map(int, j.split('x')))
        arr = list((2*(dim[0]+dim[1]), 2*(dim[1]+dim[2]), 2*(dim[2]+dim[0])))

        vol = 1 
        for k in dim:
            vol *= k
        bow = min(arr)

        total_feet += vol+bow

    print(total_feet)

part1(inputs) # part 1
part2(inputs) # part 2