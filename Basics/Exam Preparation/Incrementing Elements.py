number_of_rows = int(input())

previous_number = int(input())
number_of_rows -= 1
counter = 1
list_of_counters = []
increment = False

while number_of_rows > 0:
    number_of_rows -= 1
    current_number = int(input())
    if current_number > previous_number:
        counter += 1
        previous_number = current_number
    else:
        list_of_counters.append(counter)
        counter = 1
        previous_number = current_number

list_of_counters.append(counter)

print(max(list_of_counters))
