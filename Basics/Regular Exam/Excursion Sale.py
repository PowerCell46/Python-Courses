number_of_sea_excursions = int(input())
sea_excursion_price = 680

number_of_mountain_excursions = int(input())
mountain_excursion_price = 499

sum = 0

while number_of_sea_excursions != 0 or number_of_mountain_excursions != 0:
    current_package = str(input())
    if current_package == "Stop":
        break

    if current_package == "sea" and number_of_sea_excursions > 0:
        number_of_sea_excursions -= 1
        sum += sea_excursion_price
    elif current_package == "mountain" and number_of_mountain_excursions > 0:
        number_of_mountain_excursions -= 1
        sum += mountain_excursion_price

if number_of_sea_excursions == 0 and number_of_mountain_excursions == 0:
    print("Good job! Everything is sold.")

print(f'Profit: {sum} leva.')
