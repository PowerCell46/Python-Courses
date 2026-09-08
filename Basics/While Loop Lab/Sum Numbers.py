goal_number = int(input())

sum = 0
while sum < goal_number:
    input_number = int(input())
    sum += input_number

if sum >= goal_number:
    print(sum)
