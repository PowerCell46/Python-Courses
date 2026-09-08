import time
import random
# First task
x = 5
y = 10
print(f'\nX = {x}')
print(f'X id: {id(x)} \n')
print(f'Y = {y}')
print(f'Y id: {id(y)} \n')
x = 10
print(f'X = {x}')
print(f'X id: {id(x)} \n')
z = x
print(f'Z = {z}')
print(f'Z id: {id(z)} \n')

time.sleep(2)
# Second task
my_string = "Днес ще празнуваме"
for index in my_string:
    print(index)

print('\n')
time.sleep(2)
# Third task

input_number = float(input("Enter a real number: "))

input_number = str(input_number)
search_index = input_number.index(".")
left_value = ""
ignore_the_zeroes = True
for x in range((search_index + 1), len(input_number)):
    if input_number[x] != str(0) or ignore_the_zeroes == False:
        left_value += input_number[x]
        ignore_the_zeroes = False

print(f'The left out value is: {left_value}')
time.sleep(2)
# Fourth task

string_of_random_numbers = ""
number_of_characters = random.randint(15, 30)
for i in range(0, number_of_characters):
    n = random.randint(1, 21)
    string_of_random_numbers += str(n) + " "

count = 0
print(f'These are the generated numbers: {string_of_random_numbers}')
list_of_random_numbers = string_of_random_numbers.split(" ")
for number in list_of_random_numbers:
    for xedni in range(1, 21):
        if number == str(xedni):
            count += 1
            break
print(f'The number of values smaller or equal to 20 is: {count}')

print("\n")
# Fifth task

input_text = str(input("Enter a text that you wish to convert to chicken language: "))
list_of_text = input_text.split(" ")
chicken_language_list = []
for i in range(0, len(list_of_text)):
    current_word = list_of_text[i].lower()
    if i == 0:
        new_current_word = "Пи" + current_word

        if len(current_word) > 1:
            if current_word[1] == "и":
                new_current_word = "П" + current_word
        if current_word[0] == "п":
            if len(current_word) > 1:
                if current_word[1] == "и":
                    new_current_word = current_word
        elif current_word[0] == "и":
            new_current_word = "П" + current_word
    else:
        new_current_word = "пи" + current_word

        if len(current_word) > 1:
            if current_word[1] == "и":
                new_current_word = "п" + current_word
        if current_word[0] == "п":
            if len(current_word) > 1:
                if current_word[1] == "и":
                    new_current_word = current_word
        elif current_word[0] == "и":
            new_current_word = "п" + current_word

    chicken_language_list.append(new_current_word)

time.sleep(1)
print(f'This is your text, converted to chicken language: \n {" ".join(chicken_language_list)}')
