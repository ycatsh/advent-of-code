import numpy as np

with open('input.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

data = [list(j) for j in inputs]
matrix = np.array(data)

numRows = len(matrix)
numColumns = len(matrix[0])
edge = numRows*2 + ((numColumns-2) * 2)
scenicScores = []
numTrees = 0

for k in range(1, numRows-1):
    for l in range(1, numColumns-1):
        height = matrix[k, l]
        row = matrix[k, :]
        col = matrix[:, l]
        u = col[:k]
        d = col[k+1:]
        r = row[l+1:]
        l = row[:l]

        l = np.flip(l)
        u = np.flip(u)

        if height > max(u):
            numTrees += 1

        elif height > max(d):
            numTrees += 1

        elif height > max(l):
            numTrees += 1

        elif height > max(r):
            numTrees += 1

        numScore = 1
        for m in [l, r, u, d]:
            counter = 0
            for n in m:
                if n < height:
                    counter += 1
                elif n >= height:
                    counter += 1
                    break

            numScore *= counter
        scenicScores.append(numScore)

numTrees += edge

print(numTrees)  # part 1
print(max(scenicScores))  # part 2
