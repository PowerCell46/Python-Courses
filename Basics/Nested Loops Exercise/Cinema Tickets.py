all_tickets = 0
student_counter = 0
standard_counter = 0
kid_counter = 0
while True:
    movie_name = str(input())
    if movie_name == "Finish":
        break
    free_seats = int(input())
    taken_setas = 0
    while True:
        current_seat = str(input())
        if current_seat == "End":
            break
        all_tickets += 1

        if current_seat == "student":
            student_counter += 1
        elif current_seat == "standard":
            standard_counter += 1
        elif current_seat == "kid":
            kid_counter += 1
        taken_setas += 1
        if taken_setas == free_seats:
            break
    percentage = taken_setas / (free_seats / 100)
    print(f'{movie_name} - {percentage:.2f}% full.')

print(f'Total tickets: {all_tickets}')
student_percentage = student_counter / (all_tickets / 100)
print(f'{student_percentage:.2f}% student tickets.')
standard_percentage = standard_counter / (all_tickets / 100)
print(f'{standard_percentage:.2f}% standard tickets.')
kids_percentage = kid_counter / (all_tickets / 100)
print(f'{kids_percentage:.2f}% kids tickets.')
