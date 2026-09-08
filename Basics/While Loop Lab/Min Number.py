input_num = str(input())
smallest_num = 1000000

while input_num != "Stop":
    input_num = int(input_num)
    if input_num < smallest_num:
        smallest_num = input_num
    input_num = str(input())

if smallest_num == 1000000:
    print()
else:
    print(smallest_num)
