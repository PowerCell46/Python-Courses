number_of_numbers = int(input())
biggest_number = -1000000000
smallest_number = 1000000000

for current_num in range(0, number_of_numbers):
    current_number = int(input())
    if current_number > biggest_number:
        biggest_number = current_number

    if current_number < smallest_number:
        smallest_number = current_number

print(f'Max number: {biggest_number}')
print(f'Min number: {smallest_number}')
