import string 

with open ('../Data/d7.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]
    
# NOT DONE 

#AND: &, OR: |, NOT: ~, XOR: ^, RSHIFT: >>, LSHIFT: <<

chars = [i for i in string.ascii_lowercase]
wires = {i:0 for i in chars} #initializing the wires  

for j in inputs:
    cmd = j.split(' ')

    if cmd[1] == 'AND' or cmd[1] == 'OR':
        pass

    if cmd[1] == 'LSHIFT' or cmd[1] == 'RSHIFT':
        pass

    if cmd[0] == 'NOT':
        pass


    