import math

number_of_pages = int(input())
pages = int(input())
number_of_days = int(input())

number_of_reading_hours = number_of_pages/ pages
number_of_reading_hours = math.trunc(number_of_reading_hours)
result = number_of_reading_hours / number_of_days

print(math.trunc(result))
