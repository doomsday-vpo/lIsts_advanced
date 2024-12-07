# Using lists comprehension, write a program that receives some text, separated by space, and takes only those words whose length is even. Print each word on a new line.

words = input().split(" ")
result = [word for word in words if len(word) % 2 == 0]
print("\n".join(result))

# Alternative solution
#
# words = input().split(" ")
# result = [word for word in words if len(word) % 2 == 0]
# print("\n".join(result))