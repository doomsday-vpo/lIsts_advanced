# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line. Program it using lists and list comprehensions.

first_sequence = input().split(", ")
second_sequence = input().split(", ")
result = [word for word in first_sequence if any(word in s for s in second_sequence)]
print(result)
