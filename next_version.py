# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
#
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number. For more clarification, see the examples below.
# Note: there will be no case in which the first number will become greater than 9.
# Complete the task using lists and list comprehensions.

def next_version(version):
    version = int("".join(version)) + 1
    return ".".join(str(version))


if __name__ == "__main__":
    version = input().split(".")
    print(next_version(version))

