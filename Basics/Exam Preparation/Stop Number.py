first_number = int(input())
second_number = int(input())
stopping_number = int(input())

print_list = []

for i in range(second_number, (first_number -1), -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == stopping_number:
            break
        else:
            print_list.append(str(i))

print(" ".join(print_list))
