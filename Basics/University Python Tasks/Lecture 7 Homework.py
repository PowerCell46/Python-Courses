import functools
import random
import time


def print_func(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.05)
    print("")

print(f'First Task')

calc_list = []
list_length = random.randint(3, 10)

for i in range(list_length):
    calc_list.append(random.randint(1, 100))

print_func(f'These are the generated numbers: {", ".join([str(num) for num in calc_list])}')

#Cycle solution
sum_of_nums = 0
for number in calc_list:
    sum_of_nums += number
print_func(f'The sum of the numbers (calculated with a cycle) is: {sum_of_nums}')

#Build-in way
print_func(f'The sum of the numbers (calculated through the build-in way sum) is: {sum(calc_list)}')

#Recursion solution
def sum_with_recursion(list, index, sum = 0):
    if index > -1:
        sum += list[index]
        index -= 1
        return sum_with_recursion(list, index, sum)
    else:
        return sum

print_func(f'The sum of the numbers (calculated with recursion) is: {sum_with_recursion(calc_list, (len(calc_list)- 1))}')

print_func(f'The sum of the numbers (calculated with the reduce method) is: {functools.reduce(lambda a, b: a+b, calc_list)}')


print("----------------------------------------------")
print(f'Second Task')

second_task_list = []
second_list_length = random.randint(5, 10)

for i in range(second_list_length):
    current_num = random.randint(0, 4)
    if current_num == 0:
        second_task_list.append(True)
    elif current_num == 1:
        second_task_list.append(False)
    else:
        second_task_list.append(random.randint(2, 100))

print_func(f'This is the generated list for the second task: {", ".join([str(num) for num in sorted(second_task_list, key=lambda x: x)])}')

cleared_list = list(filter(lambda x: isinstance(x, bool), second_task_list))
print_func(f'Using filter and lambda function we only leave the True and False values in the list: {cleared_list}')

true_list_2 = list(filter(lambda x: x == True, second_task_list))
print_func(f'Using filter and lambda function we leave only the True values in the list: {true_list_2} ')

true_list = [element for element in second_task_list if element == True]
print_func(f'Using a simple comprehension we leave only the True values in the list: {true_list}')

print_func(f'To find how many times True is in the list we use len() to the previous filter and lambda list: {len(list(filter(lambda x: x == True, second_task_list)))}')
