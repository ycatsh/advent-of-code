from collections import Counter

with open('../data/06.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

def part1(data):
    chars = (Counter(i).most_common() for i in zip(*data))
    msg = ''.join(i[0][0] for i in chars)
    print(msg)

def part2(data):
    chars = (Counter(i).most_common() for i in zip(*data))
    msg = ''.join(i[-1][0] for i in chars)
    print(msg)

part1(inputs) # part 1
part2(inputs) # part 2
