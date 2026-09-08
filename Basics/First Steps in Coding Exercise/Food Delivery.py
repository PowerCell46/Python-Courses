number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

chicken_price = number_of_chicken_menus * 10.35
fish_price = number_of_fish_menus * 12.40
vegetarian_price = number_of_vegetarian_menus * 8.15
sum = chicken_price + fish_price + vegetarian_price
dessert = (sum /100) * 20
result = sum + dessert + 2.50

print(round(result, 2))
