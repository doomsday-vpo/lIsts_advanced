# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint
# •	Use the pop() and insert() methods.
#
#


notes = []

while True:
    command = input()
    if command == "End":
        break
    notes.append(command)
sorted_notes = []

for note in notes:
    importance, task = note.split("-")
    sorted_notes.append((int(importance), task))
sorted_notes.sort()
final_notes = [task for importance, task in sorted_notes]

print(final_notes)
