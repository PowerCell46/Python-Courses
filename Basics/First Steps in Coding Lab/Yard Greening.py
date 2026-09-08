yards = float(input())
price = yards * 7.61
discount = ((price / 100) * 18)
final_price = price - discount
print(f'The final price is: {round(final_price, 2)} lv.')
print(f'The discount is: {round(discount, 2)} lv.')
