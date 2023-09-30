import numpy as np

with open('../data/08.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

data = [list(j) for j in inputs]
matrix = np.array(data)

num_rows = len(matrix)
num_cols = len(matrix[0])
edge = num_rows*2 + ((num_cols-2) * 2)
scenic_scores = []
num_trees = 0

for k in range(1, num_rows-1):
    for l in range(1, num_cols-1):
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
            num_trees += 1

        elif height > max(d):
            num_trees += 1

        elif height > max(l):
            num_trees += 1

        elif height > max(r):
            num_trees += 1

        score = 1
        for m in [l, r, u, d]:
            counter = 0
            for n in m:
                if n < height:
                    counter += 1
                elif n >= height:
                    counter += 1
                    break

            score *= counter
        scenic_scores.append(score)

num_trees += edge


print(num_trees) # part 1
print(max(scenic_scores)) # part 2
