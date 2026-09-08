import math

number_of_tournaments = int(input())
starting_points = int(input())

win_counter = 0
f_counter = 0
sf_counter = 0
sum_result = 0
for index in range(0, number_of_tournaments):
    current_result = str(input())

    if current_result == "W":
        win_counter += 1
        starting_points += 2000
        sum_result += 2000
    elif current_result == "F":
        f_counter += 1
        starting_points += 1200
        sum_result += 1200
    elif current_result == "SF":
        sf_counter += 1
        starting_points += 720
        sum_result += 720


one_percent = number_of_tournaments / 100
win_counter = win_counter / one_percent
sum_result = sum_result / number_of_tournaments
print(f'Final points: {starting_points}')
print(f'Average points: {math.floor(sum_result)}')
print(f'{win_counter:.2f}%')
