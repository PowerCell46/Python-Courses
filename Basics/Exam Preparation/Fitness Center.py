number_of_visitors = int(input())
number_of_visitors_1 = number_of_visitors

back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0
workout_counter = 0
protein_counter = 0

while number_of_visitors > 0:
    number_of_visitors -= 1
    current_input = str(input())
    if current_input == "Back":
        back_counter += 1
        workout_counter += 1
    elif current_input == "Chest":
        chest_counter += 1
        workout_counter += 1
    elif current_input == "Legs":
        legs_counter += 1
        workout_counter += 1
    elif current_input == "Abs":
        abs_counter += 1
        workout_counter += 1
    elif current_input == "Protein shake":
        protein_shake_counter += 1
        protein_counter += 1
    elif current_input == "Protein bar":
        protein_bar_counter += 1
        protein_counter += 1

print(f'{back_counter} - back')
print(f'{chest_counter} - chest')
print(f'{legs_counter} - legs')
print(f'{abs_counter} - abs')
print(f'{protein_shake_counter} - protein shake')
print(f'{protein_bar_counter} - protein bar')
print(f'{(workout_counter / (number_of_visitors_1 / 100)):.2f}% - work out')
print(f'{(protein_counter / (number_of_visitors_1 / 100)):.2f}% - protein')
