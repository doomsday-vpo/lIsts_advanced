# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
#
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

def check_employee_happiness(happiness_string, factor):
    happiness_list = list(map(int, happiness_string.split()))
    improved_happiness = [h * factor for h in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(1 for h in improved_happiness if h >= average_happiness)
    total_count = len(improved_happiness)

    if happy_count >= total_count / 2:
        print(f"Score: {happy_count}/{total_count}. Employees are happy!")
    else:
        print(f"Score: {happy_count}/{total_count}. Employees are not happy!")

happiness_string = input()
factor = int(input())
check_employee_happiness(happiness_string, factor)

