input_num = str(input())
biggest_num = -1000000

while input_num != "Stop":
    input_num = int(input_num)
    if input_num > biggest_num:
        biggest_num = input_num
    input_num = str(input())

if biggest_num == -1000000:
    print()
else:
    print(biggest_num)
