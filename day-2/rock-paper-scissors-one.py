strategy_guide = open("input.txt", "r")

my_score = 0

for line in strategy_guide:
    their_play = str(line[0])
    my_play = str(line[2])

    if my_play == 'X': # Rock
        my_score += 1

        if their_play == 'A': # Rock draws with Rock
            my_score += 3
        elif their_play == 'C': # Rock beats Scissors
            my_score += 6


    elif my_play == 'Y': # Paper
        my_score += 2

        if their_play == 'A': # Paper beats Rock
            my_score += 6
        elif their_play == 'B': # Paper draws with Paper
            my_score += 3
    
    elif my_play == 'Z': # Scissors
        my_score += 3

        if their_play == 'B': # Scissors beats Paper
            my_score += 6
        elif their_play == 'C': # Scissors draws with Scissors
            my_score += 3

print(my_score)