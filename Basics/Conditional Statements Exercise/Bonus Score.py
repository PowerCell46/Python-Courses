number_of_points = int(input())
bonus = 0

if number_of_points <= 100:
    bonus += 5;
elif number_of_points > 100 and number_of_points <= 1000:
    bonus +=((number_of_points / 100) * 20)
elif number_of_points > 1000:
    bonus += (number_of_points / 10)

if number_of_points % 2 == 0:
    bonus += 1
elif number_of_points % 5 == 0:
    bonus +=  2

print(bonus)
print(number_of_points + bonus)
