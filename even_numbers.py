# Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.
# Read the string, split it, and convert the list of strings into a list of numbers using map function.
# Use a map function to iterate over the list to find all the even numbers, and add their indices.
# Use the filter function to filter only the indices and print the result.

numbers = list(map(int, input().split(", ")))

even_indices = list(filter(lambda index: numbers[index] % 2 == 0, range(len(numbers))))

print(even_indices)