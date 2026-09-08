player_name = str(input())
points = 301

unsuccessful_throws = 0
successful_throws = 0

while points > 0:
    field = str(input())
    if field == "Retire":
        print(f'{player_name} retired after {unsuccessful_throws} unsuccessful shots.')
        break
    current_points = str(input())
    if current_points == "Retire":
        print(f'{player_name} retired after {unsuccessful_throws} unsuccessful shots.')
        break
    current_points = int(current_points)

    if field == "Single":
        current_points = current_points
    elif field == "Double":
        current_points *= 2
    elif field == "Triple":
        current_points *= 3

    if current_points <= points:
        points -= current_points
        successful_throws += 1
    else:
        unsuccessful_throws += 1

if points == 0:
    print(f'{player_name} won the leg with {successful_throws} shots.')
