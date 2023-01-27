import hashlib

secret_key = 'ckczppom'

def part1(i):
    while i >= 0:
        hexed = hashlib.md5('{}{}'.format(secret_key, i).encode('utf-8')).hexdigest()
        if str(hexed)[0:5] == '00000':
            print(i)
            break
        i += 1


def part2(j):
    while j >= 0:
        hexed = hashlib.md5('{}{}'.format(secret_key, j).encode('utf-8')).hexdigest()
        if str(hexed)[0:6] == '000000':
            print(j)
            break
        j += 1

part1(0) # part 1
part2(0) # part 2