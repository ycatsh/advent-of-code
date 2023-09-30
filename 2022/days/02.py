with open('../data/02.txt') as file:
    inputs = [i for i in file.read().strip().split('\n')]

def part1(data):
    score = 0

    for j in data:
        if j[2] == 'X':
            score += 1  # rock
        if j[2] == 'Y':
            score += 2  # paper
        if j[2] == 'Z':
            score += 3  # scissors

        if j == "A X":
            score += 3  # draw
        if j == "B X":
            score += 0  # lose
        if j == "C X":
            score += 6  # win

        if j == "A Y":
            score += 6  # win
        if j == "B Y":
            score += 3  # draw
        if j == "C Y":
            score += 0  # lose

        if j == "A Z":
            score += 0  # lose
        if j == "B Z":
            score += 6  # win
        if j == "C Z":
            score += 3  # draw

    print(score)

def part2(data):
    score = 0

    for j in data:
        if j == "A X":
            score += (0+3)  # lose, scissors
        if j == "B X":
            score += (0+1)  # lose, rock
        if j == "C X":
            score += (0+2)  # lose, paper

        if j == "A Y":
            score += (3+1)  # draw, rock
        if j == "B Y":
            score += (3+2)  # draw, paper
        if j == "C Y":
            score += (3+3)  # draw, scissors

        if j == "A Z":
            score += (6+2)  # win, paper
        if j == "B Z":
            score += (6+3)  # win, scissors
        if j == "C Z":
            score += (6+1)  # win, rock

    print(score)


part1(inputs) # part 1
part2(inputs) # part 2
