year_tax = int(input())
shoes = year_tax - ((year_tax / 100) * 40)
suit = shoes - ((shoes / 100) * 20)
ball = suit / 4
accessories = ball / 5
sum = year_tax + shoes + suit + ball + accessories

print(round(sum, 2))
