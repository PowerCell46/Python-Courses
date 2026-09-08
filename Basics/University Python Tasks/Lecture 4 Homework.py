import random
import time

# first task

my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list_2 = []

for i in range(1, 11):
    my_list_2.append(i)

my_list_3 = []

my_list_3.append(1)
my_list_3.append(2)
my_list_3.append(3)
my_list_3.append(4)
my_list_3.append(5)
my_list_3.append(6)
my_list_3.append(7)
my_list_3.append(8)
my_list_3.append(9)
my_list_3.append(10)

# second task

input_number = int(input("Enter a number that you wish to reverse: "))
str_number = str(input_number)[::-1]
time.sleep(1)
print(str_number)
time.sleep(2)

input_number = int(input("Enter a number that you wish to reverse: "))
reverse_number = ""
time.sleep(1)
input_number = str(input_number)

for i in range((len(input_number) -1), -1, -1):
    reverse_number += input_number[i]

print(reverse_number)
time.sleep(2)

# third task

string_of_random_numbers = ""

number_of_generated_numbers = random.randint(15, 30)

for i in range(0, number_of_generated_numbers):
    current_generated_number = random.randint(1, 20)
    string_of_random_numbers += str(current_generated_number) + " "

print(f'The number of generated numbers is: {number_of_generated_numbers}')
time.sleep(1)
print(f'These are the generated numbers: {string_of_random_numbers}')

list_of_numbers = string_of_random_numbers.split(" ")
counter = 0
list_of_numbers.pop() # с този pop махаме последното празно пространство от листа.

for i in range(0, len(list_of_numbers)):
    current_number = int(list_of_numbers[i])
    for index in range(0, 21):
        if index == current_number:
            counter += 1
            break
time.sleep(1)
print(f'The number of generated numbers is: {counter}')
time.sleep(2)

# fourth task

input_text = str(input("Enter a text that you wish to be translated to Chicken language: "))
time.sleep(3)
list_of_the_text = input_text.split(" ")
final_text = ""

for i in range(0, len(list_of_the_text)):
    final_current_word = ""
    current_word = list_of_the_text[i]
    for index in range(0, len(current_word)):
        if i == 0 and index == 0:
            final_current_word += "Пи" + current_word[index]
        else:
            final_current_word += "пи" + current_word[index]
    final_text += final_current_word + " "

print(f'This is your text translated to Chicken language: {final_text}')
time.sleep(3)

# fifth task

manipulate_list = []

input_element_1 = input("Enter an element that you wish to add to the list: ")
manipulate_list.append(input_element_1)

input_element_1 = input("Enter an element that you wish to add to the list: ")
manipulate_list.append(input_element_1)

time.sleep(1)
print(f'This is the list until now: {manipulate_list}')

input_index = int(input("Enter a valid index where you want to put the next element: "))
input_element_2 = input("Enter an element that you wish to add to the given index: ")

time.sleep(1)
if input_index >= 0 and input_index <= len(manipulate_list):
    manipulate_list.insert(input_index, input_element_2)
    print(manipulate_list)
else:
    print("You have given an invalid index and wasted the command. Sorry!")

remove_element = str(input("Enter the element that you wish to delete from the list: "))
remove_index = manipulate_list.index(remove_element)

time.sleep(1)
if remove_index != -1:
    manipulate_list.pop(remove_index)
    print(manipulate_list)
    print(f'You successfully removed {remove_element} from the list!')

time.sleep(1)
type_of_order = str(input("How do you want to order the list by its elements length? Increasingly or Decreasingly? "))

if type_of_order == "Increasingly":
    if len(manipulate_list[0]) > len(manipulate_list[1]):
        first_item = manipulate_list[0]
        second_item = manipulate_list[1]
        manipulate_list = []
        manipulate_list = [second_item, first_item]
        print(f'This is the list after the new order: {manipulate_list}')
    else:
        print(f'{manipulate_list} - It is already ordered that way.')
elif type_of_order == "Decreasingly":
    if len(manipulate_list[0]) < len(manipulate_list[1]):
        first_item = manipulate_list[0]
        second_item = manipulate_list[1]
        manipulate_list = []
        manipulate_list = [second_item, first_item]
        print(f'This is the list after the new order: {manipulate_list}')
    else:
        print(f'{manipulate_list} - It is already ordered that way.')
else:
    print("You have entered a wrong type of order and wasted the command. Sorry!")

time.sleep(1)
set_converter = str(input("Do you wish to convert your list to a Set? Y/N"))

if set_converter == "Y":
    my_set = set()
    for i in range(0, len(manipulate_list)):
        current_el = manipulate_list[i]
        my_set.add(current_el)
    print(f'Here is your list converted to a Set: {my_set}')
else:
    print(f'Ok, here is your list anyway: {manipulate_list}')

time.sleep(1)
list_converter = str(input("Do you wish to convert back to a list the current Set? Y/N"))

if list_converter == "Y":
    manipulate_list = []
    for i in my_set:
        manipulate_list.append(i)
    print(f'Here is your set converted back to a list: {manipulate_list}')
else:
    print(f'Ok, here is your set anyway: {my_set}')

time.sleep(5)
print('Thanks for using our mini-task!')
