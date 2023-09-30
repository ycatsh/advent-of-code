with open('../data/08.txt') as file:
    input = file.read().strip().split('\n')

jump_ins = {}
max_ever = 0

for i in range(len(input)):
    ins = input[i].split(' ')
    for j in range(len(ins)):
        if j in [0, 4]:
            if ins[j] not in jump_ins:
                jump_ins[ins[j]] = 0

    if eval(f"{jump_ins[ins[4]]} {ins[5]} {ins[6]}"):
        if ins[1] == "inc":
            if jump_ins[ins[0]] > max_ever:
                max_ever = jump_ins[ins[0]]
            jump_ins[ins[0]] += int(ins[2])
        else:
            jump_ins[ins[0]] -= int(ins[2])

print(max(jump_ins.values())) # Part 1
print(max_ever) # Part 2
