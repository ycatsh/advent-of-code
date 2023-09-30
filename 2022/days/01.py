with open('../data/01.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n\n')]

calories = []

for i in inputs:
    elf = 0
    for j in i.split('\n'):
        elf += int(j)
    calories.append(elf)

calories = sorted(calories)

print(max(calories))  # part 1
print(calories[-3]+calories[-2]+calories[-1])  # part 2
