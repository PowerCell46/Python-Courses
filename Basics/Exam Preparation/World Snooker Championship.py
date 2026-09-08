type_of_match = str(input())
type_of_ticket = str(input())
number_of_tickets = int(input())
photo_with_the_trophy = str(input())


price = 0

if type_of_match == "Quarter final":
    if type_of_ticket == "Standard":
        price = 55.50
    elif type_of_ticket == "Premium":
        price = 105.20
    elif type_of_ticket == "VIP":
        price = 118.90

elif type_of_match == "Semi final":
    if type_of_ticket == "Standard":
        price = 75.88
    elif type_of_ticket == "Premium":
        price = 125.22
    elif type_of_ticket == "VIP":
        price = 300.40

elif type_of_match == "Final":
    if type_of_ticket == "Standard":
        price = 110.10
    elif type_of_ticket == "Premium":
        price = 160.66
    elif type_of_ticket == "VIP":
        price = 400

sum_for_the_group = price * number_of_tickets
photo_with_the_trophy_price = 40

if sum_for_the_group > 4000:
    sum_for_the_group -= ((sum_for_the_group / 100) * 25)
    photo_with_the_trophy_price = 0

elif sum_for_the_group > 2500:
    sum_for_the_group -= (sum_for_the_group / 10)

if photo_with_the_trophy == "Y":
    sum_for_the_group += (photo_with_the_trophy_price * number_of_tickets)

print(f'{sum_for_the_group:.2f}')
