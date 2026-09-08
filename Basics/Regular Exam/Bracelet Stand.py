pocket_money_for_a_day = float(input())
won_money_for_a_day = float(input())
spent_money_for_the_whole_time = float(input())
price_of_the_gift = float(input())

sum_of_collected_money = pocket_money_for_a_day * 5 + won_money_for_a_day * 5 - spent_money_for_the_whole_time

if sum_of_collected_money >= price_of_the_gift:
    print(f'Profit: {sum_of_collected_money:.2f} BGN, the gift has been purchased.')
else:
    needed_money = price_of_the_gift - sum_of_collected_money
    print(f'Insufficient money: {needed_money:.2f} BGN.')
