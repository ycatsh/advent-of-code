with open('../Data/d6.txt') as file:
    inputs = file.read()

# part 1
for i in range(len(inputs)-4):
    # print(set(inputs[i:i+4]))
    if len((set(inputs[i:i+4]))) == 4:
        print(i+4)
        break

# part 2
for j in range(len(inputs)-14):
    if len((set(inputs[j:j+14]))) == 14:
        print(j+14)
        break
