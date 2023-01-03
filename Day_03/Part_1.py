"""
1. Initialize a variable called value with initial value of 0
2. For each line in the input:
    1. Split that line into two halves with the same length.
    2. For each letter is in the first half:
        1. If the letter in the first half is in the second half:
            1. If the letter is uppercase: 
                value += (ord(letter) - ord('A') + 27)
               Else: 
                value += (ord(letter) - ord('a') + 1)
            2. Break the for loop
3. Print out the value
"""

if __name__ == '__main__':
    with open("./Day_03/input.txt") as file:
        data = file.read().strip().split('\n')
    
    value = 0

    for line in data:
        first_half, second_half = line[0 : len(line) // 2], line[len(line) // 2:]

        for first_half_letter in first_half:        
            if first_half_letter in second_half:
                if first_half_letter.isupper(): 
                    value += (ord(first_half_letter) - ord('A') + 27)
                else:
                    value += (ord(first_half_letter) - ord('a') + 1)

                break
    
    print(value)