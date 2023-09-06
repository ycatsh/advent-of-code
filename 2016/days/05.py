import hashlib

door_id = 'ojvtpuvg'

def part1(key, i):
    pwd = ''
    while len(pwd)<8:
        hexed = hashlib.md5(f'{key}{i}'.encode('utf-8')).hexdigest()
        if str(hexed)[0:5] == '00000':
            pwd += str(hexed)[5]
        i += 1

    print(pwd)

def part2(key, i):
    tmp = ['_', '_', '_', '_', '_', '_', '_', '_']
    pwd = ''
    while '_' in tmp:
        hexed = hashlib.md5(f'{key}{i}'.encode('utf-8')).hexdigest()
        if str(hexed)[0:5] == '00000':
            try:
                index = int(str(hexed)[5])
            except ValueError:
                pass
            char = str(hexed)[6]
  
            if index <= 7:
                if tmp[index] == '_':
                    tmp[index] = char

        i += 1

    for s in tmp:
        pwd += s

    print(pwd)

part1(door_id, 0) # part 1 
part2(door_id, 0) # part 2

