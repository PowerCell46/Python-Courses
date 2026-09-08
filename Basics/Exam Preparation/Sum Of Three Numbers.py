list_of_numbers = []

first_num = int(input())
list_of_numbers.append(first_num)
second_num = int(input())
list_of_numbers.append(second_num)
third_num = int(input())
list_of_numbers.append(third_num)

biggest_num = max(list_of_numbers)
list_of_numbers.pop(list_of_numbers.index(biggest_num))
smallest_num = min(list_of_numbers)
list_of_numbers.pop(list_of_numbers.index(smallest_num))

if smallest_num + list_of_numbers[0] == biggest_num:
    print(f'{smallest_num} + {list_of_numbers[0]} = {biggest_num}')
else:
    print("No")
    
