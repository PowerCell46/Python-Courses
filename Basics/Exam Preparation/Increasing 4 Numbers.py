starting_number = int(input())
ending_number = int(input())

if ending_number - starting_number < 3:
    print("No")

else:
    first_number = starting_number
    second_number = first_number + 1
    third_number = second_number + 1
    fourth_number = third_number + 1

    for i in range(first_number, ending_number - 2):

        for index in range(second_number, ending_number - 1):

            for x in range(third_number, ending_number):

                for xedni in range(fourth_number, ending_number + 1):
                    if x == xedni or index == x or i == index or i >= index or index >= x or x >= xedni:
                        third_number = fourth_number
                    else:
                        print(f'{i} {index} {x} {xedni}')
