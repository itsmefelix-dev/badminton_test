import random

numbers = list(range(1, 13))  # numbers from 1 to 12
random.shuffle(numbers)  # randomly shuffle the list

group1 = numbers[:4]
group2 = numbers[4:8]
group3 = numbers[8:]

print("Group 1:", group1)
print("Group 2:", group2)
print("Group 3:", group3)
