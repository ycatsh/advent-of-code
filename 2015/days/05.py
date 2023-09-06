with open ('../data/05.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

vowels = ['a', 'e', 'i', 'o', 'u']
exceptions = ['ab', 'cd', 'pq', 'xy']

def part1(data):
    nice_words = 0
    for word in data:
        #vowels, twice in a row, and exceptions 
        if len([v for v in word if v in vowels]) >= 3 and len([t for t in range(len(word)-1) if word[t]==word[t+1]])>0 and not any([e in word for e in exceptions]):
            nice_words += 1

    print(nice_words)

def part2(data):
    nice_words_p2 = 0
    for word in data:
        # pair of letters and 'xyx' type
        if len([tp for tp in range(len(word)-2) if word[tp]+word[tp+1] in word[tp+2:]])>0 and len([ro for ro in range(len(word)-2) if word[ro] == word[ro+2]])>0:
            nice_words_p2 += 1

    print(nice_words_p2)

part1(inputs) # part 1
part2(inputs) # part 2 
