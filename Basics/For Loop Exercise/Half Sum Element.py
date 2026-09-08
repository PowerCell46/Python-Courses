import math

number_of_numbers = int(input())
list = []

for current_number in range(0, number_of_numbers):
    current_num = int(input())
    list.append(current_num)

max_num = max(list)
list.remove(max_num)

sum = 0

for index in range(0, len(list)):
    number = list[index]
    sum += number

if max_num == sum:
    print(f'Yes')
    print(f'Sum = {sum}')
else:
    print(f'No')
    difference = math.fabs(max_num - sum)
    difference = math.trunc(difference)
    print(f'Diff = {difference}')
