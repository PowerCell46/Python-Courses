import math

n = int(input())

for power in range(0, n + 1, 2):
    current_num = math.pow(2, power)
    current_num = math.trunc(current_num)
    print(current_num)
