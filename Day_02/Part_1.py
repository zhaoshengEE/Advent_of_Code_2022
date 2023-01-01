"""
For opponent: A for Rock, B for Paper, and C for Scissors
For me: X for Rock, Y for Paper, and Z for Scissors.

Score scheme: (1 for Rock, 2 for Paper, and 3 for Scissors)
(0 if I lost, 3 if the round was a draw, and 6 if I won)

1. Initialize a variable named my_score with value of 0
2. Initialize a dictionary called score_scheme with the following key-value pairs:
    {'X' : 1, 'Y': 2, 'Z' : 3, 'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
3. Iterate through every single line in the input
    1. For each line of input, split that line into opponent_chioce and my_choice
    2. my_score += (score_scheme[my_choice] + score_scheme[opponent_chioce + my_choice])
4. Print out my_score
"""

if __name__ == '__main__':
    with open("./Day_02/input.txt") as file:
        data = file.read().strip().split('\n')
    
    my_score = 0
    
    score_scheme = {'X' : 1, 'Y': 2, 'Z' : 3, 'AX': 3, 'AY': 6, \
        'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
    
    for line in data:
        opponent_chioce, my_choice = line.split(' ')
        my_score += (score_scheme[my_choice] + score_scheme[opponent_chioce + my_choice])
    
    print(my_score)