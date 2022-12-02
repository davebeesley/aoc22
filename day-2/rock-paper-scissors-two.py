strategy_guide = open("input.txt", "r")

my_score = 0

for line in strategy_guide:
    their_play = str(line[0])
    my_play = str(line[2])

    if my_play == 'X': # Lose
        my_score += 0

        if their_play == 'A': # They play Rock, I play Scissors
            my_score += 3
        elif their_play == 'B': # They play Paper, I play Rock
            my_score += 1
        elif their_play == 'C': # They play Scissors, I play Paper
            my_score += 2


    elif my_play == 'Y': # Draw
        my_score += 3

        if their_play == 'A': # They play Rock, I play Rock
            my_score += 1
        elif their_play == 'B': # They play Paper, I play Paper
            my_score += 2
        elif their_play == 'C': # They play Scissors, I play Scissors
            my_score += 3
    
    elif my_play == 'Z': # Win
        my_score += 6

        if their_play == 'A': # They play Rock, I play Paper
            my_score += 2
        elif their_play == 'B': # They play Paper, I play Scissors
            my_score += 3
        elif their_play == 'C': # They play Scissors, I play Rock
            my_score += 1

print(my_score)