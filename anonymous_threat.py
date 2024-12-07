# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and unbelievably clever merging and dividing data into partitions.
# As the lead security developer in the CIA, you have been tasked to analyze the software of the virus and observe its actions on the data.
# You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace.
# Then you will begin receiving commands in one of the following formats:
# •	merge {startIndex} {endIndex}
# •	divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small substrings with equal length.
# The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.
# Input
# •	The first input line will contain the array of data.
# •	On the next several input lines, you will receive commands in the format specified above.
# •	The input ends when you receive the command "3:1".
# Output
# •	As output, you must print a single line containing the elements of the array, joined by a space.
# Constraints
# •	The strings in the array may contain any ASCII character except whitespace.
# •	The startIndex and the endIndex will be in the range [-1000…1000].
# •	The endIndex will always be greater than the startIndex.
# •	The index in the divide command will always be inside the array.
# •	The partitions will be in the range [0…100].
# •	Allowed working time/memory: 100ms / 16MB.

def merge_elements(arr, start, end):
    # Ensure indices are within the bounds of the list
    start = max(0, start)
    end = min(len(arr) - 1, end)

    # Merge the elements from start to end
    merged = ''.join(arr[start:end + 1])
    arr = arr[:start] + [merged] + arr[end + 1:]
    return arr


def divide_element(arr, index, partitions):
    element = arr[index]
    part_size = len(element) // partitions
    remainder = len(element) % partitions

    divided = []
    start = 0


    for i in range(partitions):
        if i < remainder:
            divided.append(element[start:start + part_size + 1])
            start += part_size + 1
        else:
            divided.append(element[start:start + part_size])
            start += part_size

    arr = arr[:index] + divided + arr[index + 1:]
    return arr


def process_commands(data):
    arr = data[0].split()
    commands = data[1:]

    for command in commands:
        if command == "3:1":
            break

        parts = command.split()
        if parts[0] == "merge":
            start = int(parts[1])
            end = int(parts[2])
            arr = merge_elements(arr, start, end)
        elif parts[0] == "divide":
            index = int(parts[1])
            partitions = int(parts[2])
            if partitions > 0:
                arr = divide_element(arr, index, partitions)

    return ' '.join(arr)


# Read the input data
data = []
data.append(input())
while True:
    command = input()
    data.append(command)
    if command == "3:1":
        break

print(process_commands(data))
