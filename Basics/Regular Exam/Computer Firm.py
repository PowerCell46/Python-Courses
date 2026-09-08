number_of_computers = int(input())

sum_of_ratings = 0
sum_of_sold_computers = 0
counter = number_of_computers

while number_of_computers > 0:
    number_of_computers -= 1
    current_input_number = str(input())
    rating = int(current_input_number[len(current_input_number) - 1])
    sum_of_ratings += rating
    number_of_sales1 = current_input_number[0]
    number_of_sales2 = current_input_number[1]
    number_of_sales = int(number_of_sales1 + number_of_sales2)

    if rating == 2:
        percentage = 0
    elif rating == 3:
        percentage = 50
    elif rating == 4:
        percentage = 70
    elif rating == 5:
        percentage = 85
    elif rating == 6:
        percentage = 100

    current_number_of_sold_computers = (number_of_sales / 100) * percentage
    sum_of_sold_computers += current_number_of_sold_computers

print(f'{sum_of_sold_computers:.2f}')
print(f'{(sum_of_ratings / counter):.2f}')
