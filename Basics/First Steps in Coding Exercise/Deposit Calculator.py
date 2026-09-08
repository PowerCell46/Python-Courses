depositSum = float(input())
time_Of_The_Deposit = int(input())
year_percentage = float(input()) / 100

sum = depositSum + time_Of_The_Deposit * ((depositSum * year_percentage) / 12)

print(sum)
