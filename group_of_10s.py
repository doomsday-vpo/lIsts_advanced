# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and
# prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.
# Hints
# •	Keep track of the group using a variable to store its max value.
# •	Create a loop and filter the elements that are less than or equal to the group boundary and remove them from the original list.
# •	Increase the boundary by 10.
# •	Loop until the given list is empty.


numbers = input().split(", ")
numbers = [int(number) for number in numbers]

group = 10
while numbers:
    current_group = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {current_group}")
    numbers = [number for number in numbers if number > group]
    group += 10

