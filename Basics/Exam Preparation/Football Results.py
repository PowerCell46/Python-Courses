first_result = input().split(":")
second_result = input().split(":")
third_result = input().split(":")

win = 0
draw = 0
lose = 0


if int(first_result[0]) > int(first_result[1]):
    win += 1
elif int(first_result[0]) == int(first_result[1]):
    draw += 1
elif int(first_result[0]) < int(first_result[1]):
    lose += 1


if int(second_result[0]) > int(second_result[1]):
    win += 1
elif int(second_result[0]) == int(second_result[1]):
    draw += 1
elif int(second_result[0]) < int(second_result[1]):
    lose += 1


if int(third_result[0]) > int(third_result[1]):
    win += 1
elif int(third_result[0]) == int(third_result[1]):
    draw += 1
elif int(third_result[0]) < int(third_result[1]):
    lose += 1

print(f'Team won {win} games.')
print(f'Team lost {lose} games.')
print(f'Drawn games: {draw}')
