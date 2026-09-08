input_sum = str(input())

sum = 0
while input_sum != "NoMoreMoney":
    input_sum = float(input_sum)
    if input_sum < 0:
        print("Invalid operation!")
        break
    else:
        sum += input_sum
        print(f'Increase: {input_sum:.2f}')
    input_sum = str(input())

print(f'Total: {sum:.2f}')
