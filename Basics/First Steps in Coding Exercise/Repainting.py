plastic = int(input())
paint = int(input())
razreditel = int(input())
number_of_hours = int(input())

paint = paint + (paint / 10)
plastic += 2
bags = 0.40

plastic = plastic * 1.50
paint = paint * 14.50
razreditel = razreditel * 5
sum = plastic + paint + razreditel + bags

number_of_hours = number_of_hours * ((sum / 100) * 30)
result = plastic + paint + razreditel + number_of_hours + bags

print(result)
