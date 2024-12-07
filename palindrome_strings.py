# On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".
#
# First, read all the strings and the searched palindrome, and we create an empty list for the found palindromes:
#
#     •    We use  the  join()   method with the reversed() method because reversed() returns an iterator, not a string, so we should make it into one.


words = input().split()
palindrome = input()

palindromes = []
for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")