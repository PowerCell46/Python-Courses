import math

series_name = str(input())
length_of_one_episode = int(input())
length_of_the_break = int(input())
lunch_time = length_of_the_break / 8
time_to_chill = length_of_the_break / 4
length_of_the_break -= (lunch_time + time_to_chill)

if length_of_one_episode <= length_of_the_break:
    left_time = length_of_the_break - length_of_one_episode
    left_time = math.ceil(left_time)
    left_time = str(left_time)
    print(f'You have enough time to watch {series_name} and left with {left_time} minutes free time.')
else:
    needed_time = length_of_one_episode - length_of_the_break
    needed_time = math.ceil(needed_time)
    needed_time = str(needed_time)
    print("You don't have enough time to watch " + series_name + ", you need " + needed_time + " more minutes.")
