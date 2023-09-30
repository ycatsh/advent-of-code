with open('../data/10.txt') as file:
    input = file.read().strip()

data = input.split(',')
data = [int(i) for i in data]
data2 = [ord(str(i)) for i in input] + [17, 31, 73, 47, 23]
nlist = [_ for _ in range(256)]

def part1():
    skip_size = 0
    pointer = 0

    for i in data:
        leng = pointer+i
        arr = []

        for j in range(pointer, leng):
            arr.append(nlist[j % len(nlist)])
        arr_rev = arr[::-1]

        for k, l in enumerate(range(pointer, leng)):
            nlist[l % len(nlist)] = arr_rev[k]

        pointer += i+skip_size
        skip_size += 1

    print(nlist[0]*nlist[1])

def part2():
    skip_size = 0
    pointer = 0

    for _ in range(64):
        for i in data2:
            leng = pointer+i
            arr = []

            for j in range(pointer, leng):
                arr.append(nlist[j % len(nlist)])
            arr_rev = arr[::-1]

            for k, l in enumerate(range(pointer, leng)):
                nlist[l % len(nlist)] = arr_rev[k]

            pointer += i+skip_size
            skip_size += 1
    
    dense = [[] for _ in range(16)]
    for index, m in enumerate(range(0, len(nlist), 16)):
        dense[index] = nlist[m]
        for n in range(1, 16):
            dense[index] ^= nlist[m+n]
        
    print(bytes(dense).hex())


#--- run part 2 after running part 1 ---#
#part1()
part2()
