current_tournament = str(input())
wins = 0
loses = 0
number_of_matches_1 = 0

while current_tournament != "End of tournaments":
    number_of_matches = int(input())

    game = 0
    while number_of_matches > 0:
        desi_team_wins = 0
        the_other_team_wins = 0
        desi_team_result = int(input())
        the_other_team_result = int(input())
        number_of_matches -= 1
        game += 1
        desi_team_wins += desi_team_result
        the_other_team_wins += the_other_team_result

        if desi_team_wins > the_other_team_wins:
            print(f'Game {game} of tournament {current_tournament}: win with {desi_team_wins - the_other_team_wins} points.')
            wins += 1
            number_of_matches_1 += 1
        elif desi_team_wins < the_other_team_wins:
            print(f'Game {game} of tournament {current_tournament}: lost with {the_other_team_wins - desi_team_wins} points.')
            loses += 1
            number_of_matches_1 += 1

    current_tournament = str(input())

print(f'{(wins / (number_of_matches_1 / 100)):.2f}% matches win')
print(f'{(loses / (number_of_matches_1 / 100)):.2f}% matches lost')
