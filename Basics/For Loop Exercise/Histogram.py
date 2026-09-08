number_of_numbers = int(input())

smallest_nums = 0
second_smallest = 0
middle_nums = 0
second_biggest = 0
biggest_nums = 0


for index in range(0, number_of_numbers):
    current_number = int(input())

    if current_number < 200:
        smallest_nums += 1
    elif current_number >= 200 and current_number < 400:
        second_smallest += 1
    elif current_number >= 400 and current_number < 600:
        middle_nums += 1
    elif current_number >= 600 and current_number < 800:
        second_biggest += 1
    elif current_number >= 800:
        biggest_nums += 1

one_percent = number_of_numbers / 100

smallest_nums = smallest_nums / one_percent
print(f'{smallest_nums:.2f}%')
second_smallest = second_smallest / one_percent
print(f'{second_smallest:.2f}%')
middle_nums = middle_nums / one_percent
print(f'{middle_nums:.2f}%')
second_biggest = second_biggest / one_percent
print(f'{second_biggest:.2f}%')
biggest_nums = biggest_nums / one_percent
print(f'{biggest_nums:.2f}%')
