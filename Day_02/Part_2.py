"""
For opponent: A for Rock, B for Paper, and C for Scissors
For me: X for lose, Y for draw, and Z for win.

Score scheme: (1 for Rock, 2 for Paper, and 3 for Scissors)
(0 if I lost, 3 if the round was a draw, and 6 if I won)

1. Initialize a variable named my_score with value of 0
2. Initialize a dictionary called score_scheme with the following key-value pairs:
    {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
3. Iterate through every single line in the input
    1. For each line of input, split that line into opponent_chioce and my_choice
    2. my_score += score_scheme[opponent_chioce + my_choice]
4. Print out my_score
"""

if __name__ == '__main__':
    with open("./Day_02/input.txt") as file:
        data = file.read().strip().split('\n')
    
    my_score = 0
    
    score_scheme = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
    
    for line in data:
        opponent_chioce, my_choice = line.split(' ')
        my_score += score_scheme[opponent_chioce + my_choice]
    
    print(my_score)