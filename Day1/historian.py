# Day 1 Historian Hysteria
# Find the total distance between the left and right list and submit the total

# Example
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# Would come back with 11

# Open file and pull data
with open('./input.txt', 'r') as file: 
    right_list = []
    left_list = []

    for line in file:
        values = line.split("   ")

        num1 = int(values[0])
        num2 = int(values[1])

        left_list.append(num1)
        right_list.append(num2)

    # Sort the lists
    left_list.sort()
    right_list.sort()
    
    # Go through and compare each line
    difference_value = 0
    total_difference = 0

    length_of_array =len(left_list)
    value = 0

    while value < length_of_array:
        difference_value = abs(int(right_list[value]) - int(left_list[value]))
        total_difference += difference_value
        value += 1

    print("total_difference: ", total_difference)

    