import random
import time

# first task

my_list_of_numbers = []

for i in range(1, 21):
    current_input_number = int(input(f'Enter number {i} in the diapazon 1-30: '))
    if current_input_number >= 1 and current_input_number < 31:
        my_list_of_numbers.append(current_input_number)
    else:
        print("The input number is invalid! ")
print(my_list_of_numbers)

print("-------------------------------")
print('\n')

# second task
time.sleep(2)

my_list = []
counter = 0
print_number_string = ""

for i in range(0, 21):
    current_random_num = random.randint(1, 60)
    if current_random_num > 1 and current_random_num < 31:
        counter += 1
        print_number_string += str(current_random_num) + " "

print(f'The percentage of characters randomly generated from 1 to 60, that are between 1 and 30 is {counter * 100 / 21:.2f}%!')
time.sleep(1)
print(f'These are the generated numbers, that are included in the given range (1-30): {print_number_string}')

print("-------------------------------")
print("\n")

# third task
time.sleep(2)

my_list_final = []
print_number_string_final = ""
final_counter = 0

for i in range(0, 21):
    current_random_num1 = random.randint(1, 40)
    if current_random_num1 > 1 and current_random_num1 < 31:
        print_number_string_final += str(current_random_num1) + " "
        my_list_final.append(current_random_num1)
        final_counter += 1

print(f'These are the generated numbers in the interval 1-40, that are smaller than 30: {print_number_string_final}')
time.sleep(1)
print(f'Their percentage from the total generated numbers is {final_counter * 100 / 20:.2f}%!')

print_double_numbers = []
for i in range(0, len(my_list_final)):
    currentNumber = my_list_final[i]
    index = i + 1
    while index < len(my_list_final):
        if currentNumber == my_list_final[index]:

            if currentNumber in print_double_numbers:
                a = 5
            else:
                print_double_numbers.append(currentNumber)
        index += 1

time.sleep(1)
print(f'\nThe number of characters that have at least one duplicate is: {len(print_double_numbers)}')

list_f = []
for i in range(0, len(print_double_numbers)):
    current_num = print_double_numbers[i]
    list_f.append(str(current_num))

time.sleep(1)
print(f'These are the duplicate numbers: {" ".join(list_f)}')
