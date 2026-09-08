annual_price_for_training = int(input())
shoes = annual_price_for_training - ((annual_price_for_training / 100) * 40)
suit = shoes - ((shoes / 100) * 20)
ball = suit / 4
accessories = ball / 5
sum = annual_price_for_training + shoes + suit + ball + accessories
print(f'{sum:.2f}')
