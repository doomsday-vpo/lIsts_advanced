# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even,
# and odd numbers on separate lines as shown below.
# Note: Zero is counted as a positive number. Print results for positive, negative, even and odd numbers.

numbers = input().split(", ")
numbers = [int(number) for number in numbers]

print("Positive:", ", ".join([str(number) for number in numbers if number >= 0]))
print("Negative:", ", ".join([str(number) for number in numbers if number < 0]))
print("Even:", ", ".join([str(number) for number in numbers if number % 2 == 0]))
print("Odd:", ", ".join([str(number) for number in numbers if number % 2 != 0]))

