# Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order. If 2 or more names have the same length, sort them in ascending order (alphabetically). Print the resulting list.
# Read the string and split it, Use a sorted() function to sort the names by their length first, and then - alphabetically, Print the final result.

names = input().split(", ")

sorted_names = sorted(names, key=lambda x: (-len(x), x))
print(sorted_names)
