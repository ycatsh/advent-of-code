with open('../Data/d4.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]


overlapFull = 0  # part 1
overlap = 0  # part 2

for j in inputs:
    frag1, frag2 = j.split(',')

    eS, eE = frag1.split('-')
    eS2, eE2 = frag2.split('-')

    if int(eS) <= int(eS2) and int(eE2) <= int(eE) or int(eS2) <= int(eS) and int(eE) <= int(eE2):
        overlapFull += 1
    # 82-87,61-88
    if int(eE) < int(eS2) or int(eS) > int(eE2):
        pass
    else:
        overlap += 1

print(overlapFull)  # part 1
print(overlap)  # part 2
