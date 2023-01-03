"""
1. Initialize a variable called value with initial value of 0
2. For i in range(len(data)):
    1. Assign three lines to three different variables (first_elf, second_elf, third_elf)
    2. For each letter in the first_elf:
        1. If the letter is in the second_elf AND third_elf:
            1. If the letter is uppercase: 
                value += (ord(letter) - ord('A') + 27)
               Else: 
                value += (ord(letter) - ord('a') + 1)
            2. Break the for loop
    3. i += 3
3. Print out the value
"""

if __name__ == '__main__':
    with open("./Day_03/input.txt") as file:
        data = file.read().strip().split('\n')
    
    value = 0

    for i in range(0, len(data), 3):
        first_elf, second_elf, third_elf = data[i], data[i + 1], data[i + 2]

        for first_elf_letter in first_elf:       
            if first_elf_letter in second_elf and first_elf_letter in third_elf:
                if first_elf_letter.isupper(): 
                    value += (ord(first_elf_letter) - ord('A') + 27)
                else:
                    value += (ord(first_elf_letter) - ord('a') + 1)

                break
    
    print(value)