"""
1. Define a variable called MAX with initial value of 0
2. Define an empty list to store calorie values
3. Iterate through data:
    1. If encountering a '\n':
        1. Sum up the calorie values stored in the list
        2. Compare the sum with the MAX
        3. If the sum is greater than max, assign the sum to MAX
        4. Empty the list
       Otherwise, store the calorie value to the list
4. Print out MAX 
"""

if __name__ == '__main__':
    with open("./Day_01/input.txt") as file:
        data = file.read().strip().split('\n')

    MAX = 0
    temp = []
    
    for value in data:
        if value == '':
            if sum(temp) > MAX:
                MAX = sum(temp)
            temp.clear()
        else:
            temp.append(int(value))

    print(MAX)