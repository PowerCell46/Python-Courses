import math

record_in_sec = float(input())
distance_in_meters = float(input())
time_for_one_meter = float(input())

final_time = time_for_one_meter * distance_in_meters
final_time += math.floor((distance_in_meters / 15)) * 12.5

if final_time < record_in_sec:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
else:
    left_behind_time = final_time - record_in_sec
    print(f'No, he failed! He was {left_behind_time:.2f} seconds slower.')
