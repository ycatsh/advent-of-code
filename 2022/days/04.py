with open('../data/04.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

overlap_full = 0
overlap = 0

for j in inputs:
    frag1, frag2 = j.split(',')
    eS, eE = frag1.split('-')
    eS2, eE2 = frag2.split('-')

    if int(eS) <= int(eS2) and int(eE2) <= int(eE) or int(eS2) <= int(eS) and int(eE) <= int(eE2):
        overlap_full += 1
    # 82-87,61-88
    if not (int(eE) < int(eS2) or int(eS) > int(eE2)):
        overlap += 1

print(overlap_full)  # part 1
print(overlap)  # part 2
