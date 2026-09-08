input_number = str(input())

for i in range(1, int(input_number[2]) + 1):
    first_number = i
    for index in range(1, int(input_number[1]) + 1):
        second_number = index
        for x in range(1, int(input_number[0]) + 1):
            third_number = x
            print(f'{first_number} * {second_number} * {third_number} = {first_number * second_number * third_number};')
