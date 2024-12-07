# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

text = input()
no_vowels = [char for char in text if char.lower() not in 'aouei']
print(''.join(no_vowels))
