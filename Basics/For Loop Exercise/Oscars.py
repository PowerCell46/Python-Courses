name_of_the_actor = str(input())
points_from_the_academy = float(input())
number_of_judges = int(input())
sum_of_points = points_from_the_academy

for index in range(0, number_of_judges):
    name_of_the_judge = str(input())
    points_from_the_judge = float(input())
    formula = (len(name_of_the_judge) * points_from_the_judge) / 2
    sum_of_points += formula
    if sum_of_points >= 1250.5:
        print(f'Congratulations, {name_of_the_actor} got a nominee for leading role with {sum_of_points:.1f}!')
        break

if sum_of_points < 1250.5:
    needed_points = 1250.5 - sum_of_points
    print(f'Sorry, {name_of_the_actor} you need {needed_points:.1f} more!')
