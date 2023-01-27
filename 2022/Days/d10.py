with open('../Data/d10.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?
cycleList = [20, 60, 100, 140, 180, 220]
signalStrength = []

X = 1
cycles = 0

for j in range(len(inputs)):
    if inputs[j] == 'noop':
        cycles += 1
        if cycles in cycleList:
            signalStrength.append(X*cycles)
    else:
        cycles += 1
        if cycles in cycleList:
            signalStrength.append(X*cycles)

        cycles += 1
        if cycles in cycleList:
            signalStrength.append(X*cycles)

        X += int(inputs[j].split(' ')[1])

print(signalStrength, sum(signalStrength))  # part 1
