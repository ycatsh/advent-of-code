with open('input.txt') as file:
    inputs = []
    for i in file.read().strip().split('\n'):
        inputs.append(i)

# 123 abc means that the current directory contains a file named abc with size 123
# dir xyz means that the current directory contains a directory named xyz
current_dir = ''
full_dir = ''

size_dir = {'/home': 0}
total_size = 0

for i in range(len(inputs)):
    line = inputs[i].split(' ')

    if line[0] == '$':  # cmd
        if line[1] == 'cd':  # change dir
            current_dir = line[2]

            if current_dir == '/':
                full_dir = '/home'
            elif current_dir == '..':
                full_dir = full_dir[:full_dir.rfind('/')]
            else:
                full_dir = full_dir+'/'+current_dir
                size_dir.update({full_dir: 0})

        if line[1] == 'ls':  # list dir
            pass

    elif line[0] == 'dir':
        pass

    else:
        size = int(line[0])
        current_dir = full_dir
        for j in range(full_dir.count('/')):
            size_dir[current_dir] += size
            current_dir = current_dir[:current_dir.rfind('/')]

for k in size_dir:
    if size_dir[k] <= 100_000:
        total_size += size_dir[k]

    space_required = 30_000_000 - (70_000_000 - size_dir['/home'])

    size_list = []
    if size_dir[k] >= space_required:
        size_list.append(size_dir[k])
        min_size = min(size_list)

print(total_size)  # part 1
print(min_size)  # part 2
