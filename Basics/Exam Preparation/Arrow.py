input_odd_number = int(input())

first_row_dots = int((input_odd_number - 1) / 2)
first_row = ""
upper_rows = ""

for i in range(0, first_row_dots):
    first_row += "."
    upper_rows += "."
for i in range(0, input_odd_number):
    first_row += "#"
    if i == 0 or i == input_odd_number - 1:
        upper_rows += "#"
    else:
        upper_rows += "."
for i in range(0, first_row_dots):
    first_row += "."
    upper_rows += "."

print(first_row)
for i in range(0, input_odd_number - 2):
    print(upper_rows)

working_row_length = input_odd_number * 2 - 1
middle_row = ""
dots = input_odd_number - 2
hashtags = int((working_row_length - dots ) / 2)
down_rows = []

for i in range(0, hashtags):
    middle_row += "#"
    down_rows.append(".")

for i in range(0, dots):
    middle_row += "."
    down_rows.append(".")

for i in range(0, hashtags):
    middle_row += "#"
    down_rows.append(".")

print(middle_row)
starting_index = 1
ending_index = len(down_rows) - 2
for i in range(1, input_odd_number):
    down_rows[starting_index] = "#"
    down_rows[ending_index] = "#"
    print("".join(down_rows))
    down_rows[starting_index] = "."
    down_rows[ending_index] = "."
    starting_index += 1
    ending_index -= 1
    
