input_number = int(input())
first_last_row = ""
middle_rows = ""
for i in range(0, input_number * 2):
    first_last_row += "-"
    if i == 0 or i == input_number * 2 - 1:
        middle_rows += "-"
    else:
        if i % 2 == 0:
            middle_rows += "/"
        else:
            middle_rows += "\\"

if input_number == 2:
    print(first_last_row)
    print(first_last_row)
else:
    print(first_last_row)
    print(middle_rows)
    print(middle_rows)
    print(first_last_row)
