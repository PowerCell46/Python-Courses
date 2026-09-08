starting_number = int(input())
ending_number = int(input())

if ending_number - starting_number < 3:
    print("No")

else:
    the_second_number_is_reached = False
    the_third_number_is_reached = False
    the_ending_number_is_reached = False
    decrement_the_third = False
    decrement_the_second = False
    first_number = starting_number - 1
    second_number = first_number + 1
    third_number = second_number + 1
    fourth_number = third_number + 1
    fourth_one_stop = False
    third_one_stop = False
    second_one_stop = False

    while first_number < second_number:
        first_number += 1

        if first_number == second_number:
            first_number = second_number
        else:
            if decrement_the_second:
                second_number -= 1
                decrement_the_second = False
            if the_second_number_is_reached:
                print(f'{first_number} {second_number} {third_number} {fourth_number}')

        while second_number < third_number and second_one_stop == False:
            second_number += 1
            if second_number == third_number:
                decrement_the_second = True
            else:
                if decrement_the_third:
                    third_number -= 1
                    decrement_the_third = False
                if the_third_number_is_reached:
                    print(f'{first_number} {second_number} {third_number} {fourth_number}')
                if second_number == ending_number - 2:
                    the_second_number_is_reached = True
                    second_one_stop = True

            while third_number < fourth_number and third_one_stop == False:
                third_number += 1
                if third_number == fourth_number:
                    decrement_the_third = True
                else:
                    if the_ending_number_is_reached:
                        print(f'{first_number} {second_number} {third_number} {fourth_number}')
                    if third_number == ending_number - 1:
                        the_third_number_is_reached = True
                        third_one_stop = True

                while fourth_number < ending_number and fourth_one_stop == False:
                    fourth_number += 1
                    print(f'{first_number} {second_number} {third_number} {fourth_number}')
                    if fourth_number == ending_number:
                        the_ending_number_is_reached = True
                        fourth_one_stop = True
                        decrement_the_third = False
                        decrement_the_second = False
