input_number = int(input())

print_output = ""

for i in range(1111, 10000):
    dividers = str(i)

    if int(dividers[0]) != 0:
        if input_number % int(dividers[0]) == 0:

            if int(dividers[1]) != 0:
                if input_number % int(dividers[1]) == 0:

                    if int(dividers[2]) != 0:
                        if input_number % int(dividers[2]) == 0:

                            if int(dividers[3]) != 0:
                                if input_number % int(dividers[3]) == 0:
                                    print_output += str(i) + " "

print(print_output)
