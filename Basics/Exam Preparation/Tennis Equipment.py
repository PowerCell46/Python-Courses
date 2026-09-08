import math

price_for_one_racket = float(input())
number_of_rackets = int(input())
price_for_a_sneaker = price_for_one_racket / 6
number_of_sneakers = int(input())
price = price_for_one_racket * number_of_rackets + price_for_a_sneaker * number_of_sneakers
price += ((price / 100) * 20)

first_print = math.floor(price / 8)
second_print = math.ceil((price / 8) * 7)

print(f'Price to be paid by Djokovic {first_print}')
print(f'Price to be paid by sponsors {second_print}')
