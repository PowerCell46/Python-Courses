number_of_bricks = int(input())
number_of_workers = int(input())
number_of_bricks_per_worker = int(input())
number_of_travels = 0

while number_of_bricks > 0:
    number_of_bricks -= number_of_workers * number_of_bricks_per_worker
    number_of_travels += 1

print(number_of_travels)
