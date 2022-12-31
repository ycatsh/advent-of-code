with open('input.txt') as file:
    inputs = []
    for i in file.read().strip().split('\n\n'):
        inputs.append(i)

sumList = []

for i in inputs:
    allSum = 0
    for j in i.split('\n'):
        allSum += int(j)
    sumList.append(allSum)

sumList = sorted(sumList)

print(max(sumList))  # part 1
print(sumList[-3]+sumList[-2]+sumList[-1])  # part 2
