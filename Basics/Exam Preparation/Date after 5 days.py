day = int(input())
month = int(input())


day += 5

if month == 4 or month == 6 or month == 7 or month == 11:

    if day >= 30:
        day -= 30
        month += 1
elif month == 2:
    if day >= 28:
        day -= 28
        month += 1
else:
    if day >= 31:
        day -= 31
        month += 1

if month == 13:
    month = 1

if month < 10:
    print(f'{day}.0{month}')
else:
    print(f'{day}.{month}')
