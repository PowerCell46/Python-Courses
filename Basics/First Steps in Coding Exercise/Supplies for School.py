number_of_pens = int(input()) * 5.80
number_of_markers = int(input()) * 7.20
listers_of_cleaning_liquid = int(input()) * 1.20
percentage_discount = int(input())
sum = number_of_pens + number_of_markers + listers_of_cleaning_liquid
sum = sum - ((sum / 100) * percentage_discount)
print(sum)
