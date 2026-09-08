start_of_the_interval = int(input())
end_of_the_interval = int(input()) + 1
magic_number = int(input())
counter = 0
the_number_is_found = False

for first in range(start_of_the_interval, end_of_the_interval):
    first_number = first
    for second in range(start_of_the_interval, end_of_the_interval):
        second_number = second
        result = first_number + second_number
        counter += 1
        if result == magic_number:
            print(f'Combination N:{counter} ({first_number} + {second_number} = {result})')
            the_number_is_found = True
            break
    if the_number_is_found == True:
        break


if the_number_is_found == False:
    print(f'{counter} combinations - neither equals {magic_number}')
