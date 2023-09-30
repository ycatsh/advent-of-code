with open('../data/06.txt') as file:
    input = file.read().strip().split('\t')

input = [int(num) for num in input]
patterns = []
i = 0

while True:
    patterns.append(input[:])
    blocks = max(input)
    i = input.index(blocks)
    input[i] = 0
    
    for j in range(i+1, i+blocks+1):
        input[j % len(input)] += 1 
    
    if input in patterns:
        k = patterns.index(input)
        break

    i += 1

print(len(patterns)) # part 1
print(len(patterns)-k) # part 2
