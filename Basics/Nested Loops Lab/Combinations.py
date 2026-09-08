input_num = int(input())
counter = 0

for i in range(0, input_num + 1):
    first_num = i
    for p in range(0, input_num + 1):
        second_num = p
        for s in range(0, input_num + 1):
            third_num = s
            if first_num + second_num + third_num == input_num:
                counter += 1

print(counter)
