input_number = int(input())
first_last_row = ""
middle_rows = ""
middle_row = ""
for i in range(0, input_number * 2):
    first_last_row += "%"
    if i == 0 or i == input_number * 2 - 1:
        middle_rows += "%"
        middle_row += "%"
    elif i == input_number - 1 or i == input_number:
        middle_row += "*"
        middle_rows += " "

    else:
        middle_rows += " "
        middle_row += " "

print(first_last_row)
if input_number % 2 == 0:
    middle_row_index = input_number / 2
    for i in range(1, input_number):
        if i == middle_row_index:
            print(middle_row)
        else:
            print(middle_rows)
else:
    middle_row_index = int(input_number // 2) + 1
    for i in range(1, input_number + 1):
        if i == middle_row_index:
            print(middle_row)
        else:
            print(middle_rows)
print(first_last_row)
