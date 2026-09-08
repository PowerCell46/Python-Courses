import math

number_of_tournaments = int(input())
starting_points = int(input())

sum_of_points = 0
number_of_tournaments_1 = number_of_tournaments
won_matches = 0

while number_of_tournaments > 0:
    number_of_tournaments -= 1
    current_result = str(input())
    if current_result == "W":
        starting_points += 2000
        sum_of_points += 2000
        won_matches += 1
    elif current_result == "F":
        starting_points += 1200
        sum_of_points += 1200
    elif current_result == "SF":
        starting_points += 720
        sum_of_points += 720


print(f'Final points: {starting_points}')
print(f'Average points: {math.floor(sum_of_points/ number_of_tournaments_1)}')
print(f'{(won_matches /(number_of_tournaments_1 / 100)):.2f}%')
