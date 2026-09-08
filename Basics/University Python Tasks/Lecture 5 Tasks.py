import random
# First Task
import time

length_of_the_list = int(input("How long do you wish to be the generated list? "))
input_list = []
input_checker = []

for i in range(0, length_of_the_list):
    number_of_generated_number = random.randint(1, 20)
    input_list.append(number_of_generated_number)
    if input_checker.count(number_of_generated_number) == 0:
        input_checker.append(number_of_generated_number)

print_string = "| "

for i in range(0, len(input_checker)):
    current_num = input_checker[i]
    print_string += str(current_num) + " is encountered " + str(input_list.count(current_num)) + " times. | "

print(input_list)
print(print_string)

#Second Task
sum_of_the_numbers = 0

for i in range(0, len(input_list)):
    sum_of_the_numbers += input_list[i]
time.sleep(1)
print(f'The sum of the numbers is: {sum_of_the_numbers}')

print("---------------------------------")
#Third Task

time.sleep(0.7)
my_set = set(input_list)
print(f'This is the list converted to a Set: {my_set}')
set_result = 0

for num in my_set:
    set_result += num
time.sleep(0.5)
print(f'The sum of the numbers in the Set is: {set_result}')

my_dict = {}
dictionary_result = 0
for i in range(0, len(input_list)):
    current_number = input_list[i]
    my_dict["num №" + str(i + 1)] = current_number
time.sleep(0.5)
print(f'This is the list converted to a Dictionary: {my_dict}')

for key, value in my_dict.items():
    dictionary_result += value

time.sleep(0.5)
print(f'The sum of the numbers from the Dictionary is: {dictionary_result}')

print("---------------------------------")
#Fourth Task

time.sleep(1)
input_number = int(input("Enter a number that you wish to convert to a binary one: "))
while input_number > 255 or input_number < 1:
    time.sleep(0.3)
    input_number = int(input("You have entered an invalid number. Enter a new one [1-255]: "))

result = ""

while input_number > 0:
    if input_number % 2 == 0:
        result += "0"
    else:
        result += "1"
    input_number = input_number // 2

my_list = [str(letter) for letter in result]

while len(my_list) < 8:
    my_list.append(str(0))

my_list.reverse()
time.sleep(1)

print(f'Your number converted to a binary one is: {"".join(my_list)}')

print("---------------------------------")
#Fifth Task

time.sleep(1)
input_text = str(input("Enter a text that you wish to convert to chicken language: "))
text_list = input_text.split(" ")
final_text = ""

for i in range(0, len(text_list)):
    current_word = text_list[i]
    final_current_word = ""

    if len(current_word) % 2 == 0:
        index = 0
        while index < len(current_word):
            first_char = current_word[index].lower()
            index += 1
            second_char = current_word[index].lower()
            if i == 0 and index - 1 == 0:
                final_current_word += "Пи" + first_char + second_char
            else:
                final_current_word += "пи" + first_char + second_char
            index += 1
    else:
        xedni = 0
        while xedni < len(current_word) - 1:
            first_char = current_word[xedni].lower()
            xedni += 1
            second_char = current_word[xedni].lower()
            xedni += 1
            if i == 0 and xedni - 2 == 0:
                final_current_word += "Пи" + first_char + second_char
            else:
                final_current_word += "пи" + first_char + second_char
        final_current_word += "пи" + current_word[xedni]

    final_text += final_current_word + " "

time.sleep(2)
print(f'Your text converted to a chicken language is: {final_text}')
