input_number = int(input())
string_input_number = str(input_number)
number_of_rows = int(string_input_number[0]) + int(string_input_number[1])
number_of_columns = int(string_input_number[0]) + int(string_input_number[2])

current_row_list = []
current_number_of_columns = number_of_columns
i = input_number

while i < 1000:
    string_number = str(i)

    if i % 5 != 0 and i % 3 != 0:
        i += int(string_input_number[2])
    else:
        if i % 5 == 0:
            i -= int(string_input_number[0])

        if i % 3 == 0:
            i -= int(string_input_number[1])

    current_number_of_columns -= 1
    current_row_list.append(str(i))
    if current_number_of_columns == 0:
        print(" ".join(current_row_list))
        current_row_list = []
        number_of_rows -= 1
        if number_of_rows == 0:
            break
        current_number_of_columns = number_of_columns
