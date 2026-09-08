input_number = int(input())
first_last_row = ""
middle_rows = ""
middle_row = ""

for i in range(0, input_number * 2):
    first_last_row += "*"
    if i == 0 or i == input_number * 2 - 1:
        middle_rows += "*"
        middle_row += "*"
    else:
        middle_rows += "/"
        middle_row += "/"

for i in range(0, input_number):
    first_last_row += " "
    middle_rows += " "
    middle_row += "|"

for i in range(0, input_number * 2):
    first_last_row += "*"
    if i == 0 or i == input_number * 2 - 1:
        middle_rows += "*"
        middle_row += "*"
    else:
        middle_rows += "/"
        middle_row += "/"

if input_number % 2 == 0:
    number_of_the_middle_row = input_number / 2 - 1
    for index in range(0, input_number):
        if index == 0 or index == input_number - 1:
            print(first_last_row)
        elif index == number_of_the_middle_row:
            print(middle_row)
        else:
            print(middle_rows)
else:
    number_of_the_middle_row = input_number // 2
    for index in range(0, input_number):
        if index == 0 or index == input_number - 1:
            print(first_last_row)
        elif index == number_of_the_middle_row:
            print(middle_row)
        else:
            print(middle_rows)


