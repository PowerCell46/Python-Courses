first_player = str(input())
second_player = str(input())

first_player_points = 0
second_player_points = 0
number_wars = False
end_of_game = False

while True:
    first_player_current_card = str(input())
    if first_player_current_card == "End of game":
        end_of_game = True
        break
    first_player_current_card = int(first_player_current_card)
    second_player_current_card = str(input())
    if second_player_current_card == "End of game":
        break
    second_player_current_card = int(second_player_current_card)

    if number_wars:
        print("Number wars!")
        if first_player_current_card > second_player_current_card:
            print(f'{first_player} is winner with {first_player_points} points')
            break
        elif second_player_current_card > first_player_current_card:
            print(f'{second_player} is winner with {second_player_points} points')
            break

    if first_player_current_card > second_player_current_card:
        first_player_points += (first_player_current_card - second_player_current_card)
    elif second_player_current_card > first_player_current_card:
        second_player_points += (second_player_current_card - first_player_current_card)
    elif first_player_current_card == second_player_current_card:
        number_wars = True

if end_of_game:
    print(f'{first_player} has {first_player_points} points')
    print(f'{second_player} has {second_player_points} points')
