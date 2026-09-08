import time
import os

print(f'First Task')
time.sleep(1)

container_type = str(input("Enter the type of container that you wish to use (list/tuple/dictionary/set): "))
first_container = input("Enter numbers for the first container, separated by comma and space: ")
second_container = input("Enter numbers for the second container, separated by comma and space: ")

first_list = []
second_list = []
common_elements = ""
first_container = first_container.split(", ")
for i in first_container:
    first_list.append(int(i))
second_container = second_container.split(", ")
for i in second_container:
    second_list.append(int(i))
time.sleep(1.5)

if container_type == "list":
    print(f'First list: {first_list}')
    print(f'Second list: {second_list}')
    for i in first_list:
        if i in second_list:
            common_elements += str(i) + " "
    time.sleep(1)
    print(f'Common elements: {common_elements}')

elif container_type == "tuple":
    first_tuple = tuple(first_list)
    second_tuple = tuple(second_list)
    print(f'First tuple: {first_tuple}')
    print(f'Second tuple: {second_tuple}')
    for i in first_tuple:
        if i in second_tuple:
            common_elements += str(i) + " "
    time.sleep(1)
    print(f'Common elements: {common_elements}')

elif container_type == "dictionary":
    first_dictionary = {}
    second_dictionary = {}
    counter = 1
    for i in first_list:
        first_dictionary["key" + str(counter)] = i
        counter += 1
    counter = 1
    for i in second_list:
        second_dictionary["key" + str(counter)] = i
        counter += 1
    print(f'First dictionary: {first_dictionary}')
    print(f'Second dictionary: {second_dictionary}')
    for i in first_dictionary.values():
        if i in second_list:
            common_elements += str(i) + " "
    time.sleep(1)
    print(f'Common elements: {common_elements}')

elif container_type == "set":
    first_set = set(first_list)
    second_set = set(second_list)
    print(f'First set: {first_set}')
    print(f'Second set: {second_set}')
    for i in first_set:
        if i in second_set:
            common_elements += str(i) + " "
    time.sleep(1)
    print(f'Common elements: {common_elements}')

print(f'-----------------------------')
time.sleep(5)
print(f'Second Task')

length_of_the_side_of_the_cube = int(input('Enter the length of the side of the cube: '))
volume_of_the_cube = length_of_the_side_of_the_cube ** 3
surface_of_the_cube = 6 * (length_of_the_side_of_the_cube ** 2)
time.sleep(1)
print(f'The volume of the cube is: {volume_of_the_cube} cm\u00b3')
time.sleep(1)
print(f'The surface of the cube is: {surface_of_the_cube} cm\u00b2 ')

print(f'-----------------------------')
time.sleep(5)
print(f'Third Task')

input_numbers_list = []
while True:
    current_input = str(input("Enter a number or type stop: "))
    if current_input == "stop":
        break
    else:
        current_input = int(current_input)
        input_numbers_list.append(current_input)

time.sleep(1.5)
def SumOfTheInputNumbers(input_list):
    sum_of_the_numbers = 0
    for num in input_list:
        sum_of_the_numbers += num
    return f'The sum of the numbers is: {sum_of_the_numbers}'
print(SumOfTheInputNumbers(input_numbers_list))

print(f'-----------------------------')
time.sleep(5)
print(f'Fourth Task')

while True:
    name = input("Enter a name which you want to add to names.txt file (quit/ delete all data): ")
    if name == 'quit':
        print("Opening...")
        time.sleep(2)
        filename = 'names.txt'
        if os.name == 'nt':  # Windows
            os.system(f'start {filename}')
        elif os.name == 'posix':  # Linux or Mac
            os.system(f'open {filename}')
        break

    if name == "delete all data":
        with open('names.txt', 'w') as f:
            f.write('')
        time.sleep(1)
        print("All of the data from the names.txt file has been successfully deleted!")
        time.sleep(1)
    else:
        with open('names.txt', 'a') as f:
            f.write(name + '\n')
        time.sleep(1)
        print(f'Name successfully added to the file!')
        time.sleep(1)
