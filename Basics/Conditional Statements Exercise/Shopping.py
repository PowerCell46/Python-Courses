budget = float(input())
number_of_videocards = int(input())
number_of_processors = int(input())
number_of_rams = int(input())

videocards_price = number_of_videocards * 250
processors_price = number_of_processors * ((videocards_price /100 ) * 35)
rams_price = number_of_rams * (videocards_price / 10)
sum = videocards_price + processors_price + rams_price

if number_of_videocards > number_of_processors:
    sum -= (sum / 100 ) * 15

if budget >= sum:
    left_money = budget - sum
    print(f'You have {left_money:.2f} leva left!')
else:
    needed_money = sum - budget
    print(f'Not enough money! You need {needed_money:.2f} leva more! ')
