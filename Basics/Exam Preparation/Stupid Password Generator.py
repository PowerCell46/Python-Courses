first_number = int(input())
second_number = int(input())

print_list = []
for i in range(1, (first_number)):
    for index in range(1, (first_number + 1)):
        for xedni in range(97, (97 + second_number)):
            for xedni_2 in range(97, (97 + second_number)):
                for final in range((i +1), (first_number +1)):
                    if final > index:
                        result = str(i) + str(index) + chr(xedni) + chr(xedni_2) + str(final)
                        print_list.append(result)

print(" ".join(print_list))
