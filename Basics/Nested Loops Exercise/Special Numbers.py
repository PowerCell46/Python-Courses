print_output = ""
input_number = int(input())
for current_num in range(1111, 9999):
    print_it = False
    current_num = str(current_num)

    for index in range(0, 4):
        current_digit = int(current_num[index])
        if current_digit == 0:
            print_it = False
            break
        if input_number % current_digit == 0:
            print_it = True
        else:
            print_it = False
            break
    if print_it == True:
        print_output += f'{current_num} '

print(print_output)
