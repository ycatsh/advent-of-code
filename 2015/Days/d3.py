with open ('../Data/d3.txt') as file:
    inputs = [i for i in file.read()]

move_dir = {'>':[1,0], '<':[-1,0], '^':[0,1], 'v':[0,-1]}


def part1(data, moves):
    house = [(0,0)]

    for i in data:
        tmp_house = house[-1]
        house.append((tmp_house[0]+moves[i][0], tmp_house[1]+moves[i][1]))

    print(len(set(house)))


def part2(data, moves):
    house = [(0,0)]
    santa_data = []

    for i in data[::2][:]:
        santa_data.append(i)
        data.remove(i)

    robot_data = data 

    for i in santa_data:
        tmp_house = house[-1]
        house.append((tmp_house[0]+moves[i][0], tmp_house[1]+moves[i][1]))

    for j in robot_data:
        tmp_house = house[-1]
        house.append((tmp_house[0]+moves[j][0], tmp_house[1]+moves[j][1]))

    #print()

part1(inputs, move_dir) # part 1
#part2(inputs, move_dir) # part 2 - not done