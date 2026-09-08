country = str(input())
item = str(input())

difficulty = 0
precision = 0

if country == "Russia":
    if item == "ribbon":
        difficulty = 9.1
        precision = 9.4
    elif item == "hoop":
        difficulty = 9.3
        precision = 9.8
    elif item == "rope":
        difficulty = 9.6
        precision = 9
        
elif country == "Bulgaria":
    if item == "ribbon":
        difficulty = 9.6
        precision = 9.4
    elif item == "hoop":
        difficulty = 9.55
        precision = 9.75
    elif item == "rope":
        difficulty = 9.5
        precision = 9.4
        
elif country == "Italy":
    if item == "ribbon":
        difficulty = 9.2
        precision = 9.5
    elif item == "hoop":
        difficulty = 9.45
        precision = 9.35
    elif item == "rope":
        difficulty = 9.7
        precision = 9.15

result = difficulty + precision
left_out_points = 100 - ((result / 20) * 100)

print(f'The team of {country} get {result:.3f} on {item}.')
print(f'{left_out_points:.2f}%')
