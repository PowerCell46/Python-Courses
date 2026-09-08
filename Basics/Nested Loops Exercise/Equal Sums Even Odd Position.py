first_num = int(input())
second_num = int(input())
print_1 = ""
for current_num in range(first_num, second_num + 1):
    current_number = str(current_num)
    sum_of_even = 0
    sum_of_odd = 0
    for index in range(0, 6):
        current_digit = current_number[index]
        current_digit = int(current_digit)
        if index % 2 == 0:
            sum_of_even += current_digit
        elif index % 2 != 0:
            sum_of_odd += current_digit
    if sum_of_odd == sum_of_even:
        current_number = str(current_number)
        print_1 += current_number + " "

print(print_1)
