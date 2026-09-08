input_number = int(input("Enter the size of the side:"))
counter = 0
for i in range(0, input_number):
    counter += 1
    if counter == 1 or counter == input_number:
        up_down_side = "*"
        for i in range(1, input_number):
            up_down_side += "*"
        print(up_down_side)
    else:
        inside_side = "*"
        for i in range(1, input_number - 1):
            inside_side += " "
        inside_side += "*"
        print(inside_side)
