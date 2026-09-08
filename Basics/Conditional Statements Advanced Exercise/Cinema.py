type_of_projection = str(input())
number_of_rows = int(input())
number_of_columns = int(input())
price_for_a_ticket = 0
 
if type_of_projection == "Premiere":
    price_for_a_ticket =12
elif type_of_projection == "Normal":
    price_for_a_ticket = 7.50
elif type_of_projection == "Discount":
    price_for_a_ticket = 5
 
final_price = (number_of_rows * number_of_columns) * price_for_a_ticket
 
print(f'{final_price:.2f} leva')
