# Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the course and all the exercises for the lessons.
#     Before the course starts, there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next course, separated by a comma and a space ", ".
# Until you receive the "course start" command, you will be given some commands to modify the course schedule.
# The possible commands are:
# •	"Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# •	"Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# •	"Remove:{lessonTitle}" - remove the lesson, if it exists.
# •	"Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# •	"Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise".
# If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.
# Input / Constraints
# •	On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
# •	Until "course start" you will receive commands in the format described above.
# Output
# •	Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
# "{lesson index}.{lessonTitle}".
# •	Allowed working time / memory: 100ms / 16MB.

lessons = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    if command[0] == "Add":
        if command[1] not in lessons:
            lessons.append(command[1])
    elif command[0] == "Insert":
        if command[1] not in lessons:
            lessons.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] in lessons:
            lessons.remove(command[1])
            if f"{command[1]}-Exercise" in lessons:
                lessons.remove(f"{command[1]}-Exercise")
    elif command[0] == "Swap":
        if command[1] in lessons and command[2] in lessons:
            first_index = lessons.index(command[1])
            second_index = lessons.index(command[2])
            lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
            if f"{command[1]}-Exercise" in lessons and f"{command[2]}-Exercise" in lessons:
                first_exercise_index = lessons.index(f"{command[1]}-Exercise")
                second_exercise_index = lessons.index(f"{command[2]}-Exercise")
                lessons[first_exercise_index], lessons[second_exercise_index] = lessons[second_exercise_index], lessons[first_exercise_index]
            elif f"{command[1]}-Exercise" in lessons:
                exercise_index = lessons.index(f"{command[1]}-Exercise")
                lessons.remove(f"{command[1]}-Exercise")
                lessons.insert(second_index + 1, f"{command[1]}-Exercise")
            elif f"{command[2]}-Exercise" in lessons:
                exercise_index = lessons.index(f"{command[2]}-Exercise")
                lessons.remove(f"{command[2]}-Exercise")
                lessons.insert(first_index + 1, f"{command[2]}-Exercise")
    elif command[0] == "Exercise":
        if command[1] in lessons:
            index = lessons.index(command[1])
            if index + 1 == len(lessons) or not lessons[index + 1].endswith("-Exercise"):
                lessons.insert(index + 1, f"{command[1]}-Exercise")
        else:
            lessons.append(command[1])
            lessons.append(f"{command[1]}-Exercise")
    command = input()

for index, lesson in enumerate(lessons, start=1):
    print(f"{index}.{lesson}")