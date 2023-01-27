data = '1321131112'
numbers = [int(i) for i in data]

def result(part, num):
    for _ in range(part):
        c = 1
        sep = []
        prev = num[0]

        for digit in num[1:]:
            if prev == digit:
                c+= 1
            else:
                sep.extend((c, prev))
                prev = digit
                c = 1
        sep.extend((c, prev))
        num = sep
        
    print(len(num))

result(40, numbers) # part 1 
result(50, numbers) # part 2