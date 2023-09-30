with open('../data/10.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?
cycles = [20, 60, 100, 140, 180, 220]
strength = []

def part1():
    X = 1
    cycle = 0
     
    for j in range(len(inputs)):
        if inputs[j] == 'noop':
            cycle += 1
            if cycle in cycles:
                strength.append(X*cycle)
        else:
            for _ in range(2):
                cycle += 1
                if cycle in cycles:
                    strength.append(X*cycle)
            X += int(inputs[j].split(' ')[1])
     
    print(sum(strength))

part1() # part 1
