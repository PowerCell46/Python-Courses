input_number = int(input())
if input_number == 1:
    print(1)
else:
    first_row = []
    current_num = ""

    for i in range(1, input_number + 1):
        first_row.append(str(i))
    print(" ".join(first_row))

    middle_rows = input_number - 2
    starting_number = input_number - middle_rows


    while middle_rows > 0:
        start_inverting = False
        current_starting_num = input_number - middle_rows
        counter = 0
        current_row_list = []

        while counter < input_number:
            current_row_list.append(str(current_starting_num))
            if current_starting_num >= input_number:
                start_inverting = True

            if start_inverting:
                current_starting_num -= 1
            else:
                current_starting_num += 1
            counter += 1
        print(" ".join(current_row_list))
        middle_rows -= 1

    last_row = []

    for i in range(input_number, 0, -1):
        last_row.append(str(i))

    print(" ".join(last_row))
