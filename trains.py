# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

wagons = [0] * int(input())
command = input()

while command != "End":
    command = command.split()
    if command[0] == "add":
        wagons[-1] += int(command[1])  # Add people to the last wagon
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
    command = input()

print(wagons)
