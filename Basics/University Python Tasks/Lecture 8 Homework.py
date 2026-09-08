import random
import time
from sty import ef, rs
import sty

print(sty.fg(200) + "First task" + sty.fg(254))
time.sleep(0.5)

list_length = random.randint(5, 100)
working_list = []
for i in range(list_length):
    working_list.append(random.randint(0, 1000))
print(f'This is the generated list:\n{working_list}')

try:
    searched_value = int(input(sty.fg(77) + "Enter a number that you wish to search for in the list: " + sty.fg(254)))
    if searched_value not in working_list:
        raise ValueError
except:
    searched_value = random.choice(working_list)
    time.sleep(0.5)
    print(sty.fg(160) + f'You have entered an invalid number, so the program chose a random one, which is: {ef.bold + str(searched_value) + rs.bold_dim + sty.fg(254)}')
    time.sleep(1)

counter = 0

while True:
    first_half = working_list[:len(working_list)//2]
    second_half = working_list[len(working_list)//2:]
    counter += 1
    if searched_value in first_half:
        working_list = first_half
    elif searched_value in second_half:
        working_list = second_half
    time.sleep(0.5)
    if len(working_list) == 1:
        print(f"Number {sty.fg(160) + ef.bold + str(searched_value) + rs.bold_dim + sty.fg(254)} was found on the {sty.fg(160) + ef.bold + str(counter) + rs.bold_dim + sty.fg(254)} turn.")
        break
    print(f'This is the list after it was cut in half: {working_list}')


time.sleep(1.5)
print(f'------------------------\n{sty.fg(200) + "Second task" + sty.fg(254)}')

try:
    operations_dict = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    first_number = int(input("Enter the first number for the second task: "))
    second_number = int(input("Enter the second number for the second task: "))
    operator = input("Enter an operator for the two numbers (+, -, *, /): ")
    print(f'The result of the operation between the two numbers is: {sty.fg(77) + str(operations_dict[operator](first_number, second_number)) + sty.fg(254)}')
except ValueError:
    print(sty.fg(160) + "You entered an invalid number and an Error occurred." + sty.fg(254))

finally:
    time.sleep(2)


print(f'------------------------\n{sty.fg(200) + "Third task" + sty.fg(254)}')

third_task_list = [False, 1, 2, 3.9, True, "ma", [1, 2], "ma", (1, 2), 5, [3, 4], False, (1, 2)]
print(third_task_list)

for _ in range(5):
    third_task_first_element = random.choice(third_task_list)
    third_task_second_element = random.choice(third_task_list)
    print(f'The first element from the list is: {third_task_first_element}\nThe second element from the list is: {third_task_second_element}')

    try:
        if ((type(third_task_first_element) == int or type(third_task_first_element) == float) and type(third_task_second_element) == bool) or ((type(third_task_second_element) == int or type(third_task_second_element) == float) and type(third_task_first_element) == bool):
            raise TypeError
        third_task_result = third_task_first_element + third_task_second_element
        print(f'The sum of the two values was a successful operation and the result is: {sty.fg(160) + str(third_task_result) + sty.fg(254)}!')
    except (ValueError, TypeError):
        print(sty.fg(160) + "The current operation is not possible" + sty.fg(254))
    finally:
        print("\n")
        time.sleep(2)


time.sleep(1.5)
print(f'------------------------\n{sty.fg(200) + "Fourth task" + sty.fg(254)}')

fourth_task_list = [["da", "ne"], False, 5, "br"]
print(fourth_task_list)

fourth_task_first_element = random.choice(fourth_task_list)
fourth_task_second_element = random.choice(fourth_task_list)
print(f'The first element from the list is: {fourth_task_first_element}\nThe second element from the list is: {fourth_task_second_element}')

try:
    fourth_task_result = fourth_task_first_element + fourth_task_second_element
    fourth_task_result += (fourth_task_first_element * fourth_task_second_element)
    print(f'The operation sum was successful and the program did not raise and error. The result from the multiplication and the sum is: {fourth_task_result} ')
except TypeError:
    try:
        fourth_task_result = (fourth_task_first_element * fourth_task_second_element)
        if len(str(fourth_task_result)) > 0:
            print(f'The operation sum was unsuccessful and the program rose an error, so the result is the multiplication of the two numbers is: {fourth_task_result}')
        else:
            print(f'The operation sum was unsuccessful and the program rose an error, the multiplication also did not work.')
    except:
        print(f'The operation sum was unsuccessful and the program rose an error, the multiplication also did not work.')
        
