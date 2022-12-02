"""
1. Define variables called Top_1, Top_2, Top_3 with initial values of 0
2. Define an empty list to store calorie values
3. Iterate through data:
    1. If encountering a '\n':
        1. Sum up the calorie values stored in the list
        2. Compare the sum with the MAX
        3. If the sum is greater than Top_1:
            1. Assign Top_2 to Top_3
            2. Assgin Top_1 to Top_2
            3. Assign the sum to Top_1
          Elif the sum is greater than Top_2:
            1. Assign Top_2 to Top_3
            2. Assign sum to Top_2
          Elif the sum is greater than Top_3:
            1. Assign sum to Top_3
        4. Empty the list
       Else, store the calorie value to the list
4. Print out Top_1 + Top_2 + Top_3 
"""

if __name__ == '__main__':
    with open("./Day_01/input.txt") as file:
        data = file.read().strip().split('\n')

    Top_1 = 0
    Top_2 = 0
    Top_3 = 0
    temp = []
    
    for value in data:
        if value == '':
            if sum(temp) > Top_1:
                Top_3 = Top_2
                Top_2 = Top_1
                Top_1 = sum(temp)
            elif sum(temp) > Top_2:
                Top_3 = Top_2
                Top_2 = sum(temp)
            elif sum(temp) > Top_3:
                Top_3 = sum(temp)
            temp.clear()
        else:
            temp.append(int(value))

    print(Top_1 + Top_2 + Top_3)