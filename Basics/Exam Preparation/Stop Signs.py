input_number = int(input())

if input_number < 3:
    print("Invalid number")
elif input_number == 3:

    middle_row = "//" + input_number * "_" + "STOP!" + input_number * "_" + "\\" + "\\"
    upper_row = "//" + input_number * "_" + 5 * "_" + input_number * "_" + "\\"
    lower_row = "\\" + input_number * "_" + 5 * "_" + input_number * "_" + "//"
    counter = input_number + 1
    top_row = counter * "." + 4 * "_" + (input_number - counter) * "_" + 3 * "_" + counter * "."
    print(top_row)
    while counter > 1:
        counter -= 1
        upper_row = counter * "." + "//" + (input_number - counter) * "_" + 5 * "_" + (
                    input_number - counter) * "_" + "\\" + "\\" + counter * "."
        print(upper_row)
    print(middle_row)
    first_lower_row = "\\" + "\\" + input_number * "_" + 5 * "_" + input_number * "_" + "//"
    print(first_lower_row)
    counter_1 = 0
    while counter_1 < input_number - 1:
        counter_1 += 1
        lower_row = counter_1 * "." + "\\" + "\\" + (input_number - counter_1) * "_" + 5 * "_" + (
                    input_number - counter_1) * "_" + "//" + counter_1 * "."
        print(lower_row)

else:
    extra_number = (input_number // 2)
    middle_row = "//" + (input_number + extra_number) * "_" + "STOP!" + (input_number + extra_number) * "_" + "\\" + "\\"
    upper_row = "//" + input_number * "_" + 5 * "_" + input_number * "_" + "\\"
    lower_row = "\\" + input_number * "_" + 5 * "_" + input_number * "_" + "//"
    counter = input_number + 1
    top_row = counter * "." + 4 * "_" + (3 + extra_number + extra_number) * "_" + counter * "."
    print(top_row)
    while counter > 1:
        counter -= 1
        upper_row = counter * "." + "//" + ((input_number - counter) + extra_number) * "_" + 5 * "_" + ((input_number - counter) + extra_number) * "_" + "\\" + "\\" + counter * "."
        print(upper_row)

    print(middle_row)

    first_lower_row = "\\" + "\\" + (input_number + extra_number) * "_" + 5 * "_" + (input_number + extra_number) * "_" + "//"
    print(first_lower_row)
    counter_1 = 0
    while counter_1 < input_number - 1:
        counter_1 += 1
        lower_row = counter_1 * "." + "\\" + "\\" + ((input_number - counter_1) + extra_number) * "_" + 5 * "_" + ((input_number - counter_1) + extra_number) * "_" + "//" + counter_1 * "."
        print(lower_row)
