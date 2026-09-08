number_of_inputs = int(input())

sum_1 = 0
sum_2 = 0
sum_3 = 0
counter = 0
counter_odd = 0

while number_of_inputs > 0:
    number_of_inputs -= 1
    current_input = int(input())
    counter += 1
    if counter % 2 == 0:
        sum_2 += current_input
    else:
        counter_odd += 1
        if counter_odd % 2 == 0:
            sum_3 += current_input
            counter -= 1
        else:
            sum_1 += current_input

print(f'sum1 = {sum_1}')
print(f'sum2 = {sum_2}')
print(f'sum3 = {sum_3}')
