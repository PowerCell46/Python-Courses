input_number = int(input())
magic_number = input_number + 1

print_result = ""

for first in range(1, magic_number):
    for second in range(1, magic_number):
        for third in range(1, magic_number):
            for forth in range(1, magic_number):
                for fifth in range(1, magic_number):
                    for sixth in range(1, magic_number):

                        if first * second * third * forth * fifth * sixth == input_number:
                            print_result += (str(first) + str(second) + str(third) + str(forth) + str(fifth) + str(sixth) + " ")

print(print_result)
