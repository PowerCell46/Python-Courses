import copy

input_number = int(input())

middle_row_list = []
reversed_middle_row_list = []

for i in range(0, input_number):
    middle_row_list.append("*")
    middle_row_list.append("-")
    reversed_middle_row_list.append("-")
    reversed_middle_row_list.append("*")

middle_row_list.pop()
reversed_middle_row_list.pop()
list_of_rows = []
middle_row_list_copy = copy.deepcopy(middle_row_list)

counter = 0

while reversed_middle_row_list.count("*") > 1 or middle_row_list.count("*") > 1:
    middle_row_list.pop(len(middle_row_list) - 1 - counter)
    middle_row_list.append(" ")
    middle_row_list.pop(counter)
    middle_row_list.insert(counter, " ")

    reversed_middle_row_list.pop(len(reversed_middle_row_list) - 1 - counter)
    reversed_middle_row_list.append(" ")
    reversed_middle_row_list.pop(counter)
    reversed_middle_row_list.insert(counter, " ")

    if counter % 2 == 0:
        copy_list = copy.deepcopy(reversed_middle_row_list)
        list_of_rows.append(copy_list)
    else:
        copy_list = copy.deepcopy(middle_row_list)
        list_of_rows.append(copy_list)
    counter += 1


for i in range(len(list_of_rows) - 1, -1, -1):
    current_row = list_of_rows[i]
    print("".join(current_row))

print("".join(middle_row_list_copy))

for i in range(0, len(list_of_rows)):
    current_row = list_of_rows[i]
    print("".join(current_row))
