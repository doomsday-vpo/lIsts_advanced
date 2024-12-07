# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)
def decipher_message(secret_message):
    words = secret_message.split()
    deciphered_words = []

    for word in words:
        i = 0
        while word[i].isdigit():
            i += 1

        first_char = chr(int(word[:i]))
        rest_of_word = word[i:]

        if len(rest_of_word) > 1:
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]

        deciphered_word = first_char + rest_of_word
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)


secret_message = input()
print(decipher_message(secret_message))
