number_of_days = int(input())
type_of_room = str(input())
grade = str(input())
number_of_nights = number_of_days - 1

price_for_the_room = 0
discount = 0

if type_of_room == "room for one person":
    price_for_the_room = 18
elif type_of_room == "apartment":
    price_for_the_room = 25

    if number_of_days < 10:
        discount = 30
    elif number_of_days >= 10 and number_of_days <= 15:
        discount = 35
    elif number_of_days > 15:
        discount = 50

elif type_of_room == "president apartment":
    price_for_the_room = 35

    if number_of_days < 10:
        discount = 10
    elif number_of_days >= 10 and number_of_days <= 15:
        discount = 15
    elif number_of_days > 15:
        discount = 20

almost_final_sum = number_of_nights * price_for_the_room - ((number_of_nights * price_for_the_room / 100) * discount)

final_discount = 0

if grade == "positive":
    final_sum = almost_final_sum + ((almost_final_sum / 100) * 25)
elif grade == "negative":
    final_sum = almost_final_sum - ((almost_final_sum / 100) * 10)

print(f'{final_sum:.2f}')
