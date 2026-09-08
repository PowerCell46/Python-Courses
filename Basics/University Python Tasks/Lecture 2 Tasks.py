import time

input_x = int(input("Write a number that you wish to multiplicate: "))
print(f'The result is: {input_x * input_x}')

# печатаме резултата от умножението на стойността

print(f'---------')


input_y = int(input("Write a number that you want to factor out: "))

result = 1
index = 1

while index <= input_y:
    result *= index
    index += 1

# пресмятаме резултата с while цикъл

print(result)

print("---------")

input_greeting = str(input("Enter the wish that you wanna make: "))
input_name = str(input("Enter your name: "))

print(f'vvvvvvvvvvvvv')
print(f'{input_greeting} {input_name}!')
print(f'^^^^^^^^^^^^^')

print("---------")

first_value = int(input("Enter the first value (number): "))
second_value = int(input("Enter the second value (number): "))

list_keeper = [first_value, second_value]
second_value = list_keeper[0]
first_value = list_keeper[1]

time.sleep(1.5)
print("###########")
print(f'The new first value is {first_value}')
print(f'The new second value is {second_value}')
