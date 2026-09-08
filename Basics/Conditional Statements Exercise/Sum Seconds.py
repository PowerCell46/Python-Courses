first = int(input())
second = int(input())
third = int(input())
sum = first + second + third
hours = sum // 60
minutes = sum % 60

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
