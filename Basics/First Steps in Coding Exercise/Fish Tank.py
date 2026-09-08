length = int(input())
width = int(input())
height = int(input())
percantage = float(input())

volume = length * width * height
liters = volume / 1000
percantage = percantage * (liters / 100)
answer = liters - percantage

print(answer)
