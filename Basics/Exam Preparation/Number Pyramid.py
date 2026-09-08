input_number = int(input())
if input_number == 1:
    print("1")
else:
    row_length = 1
    current_number = 1
    current_row_length = 0
    current_row = ""
    while True:
        current_row += str(current_number) + " "
        current_number += 1
        current_row_length += 1
        if current_row_length == row_length:
            print(current_row)
            current_row = ""
            current_row_length = 0
            row_length += 1
        if current_number == input_number:
            current_row += str(current_number)
            print(current_row)
            break

