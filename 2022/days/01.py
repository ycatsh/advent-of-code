with open('../data/01.txt') as file:
    inputs = [i for i in file.read().strip().split('\n\n')]

sumList = []

for i in inputs:
    allSum = 0
    for j in i.split('\n'):
        allSum += int(j)
    sumList.append(allSum)

sumList = sorted(sumList)

print(max(sumList))  # part 1
print(sumList[-3]+sumList[-2]+sumList[-1])  # part 2
