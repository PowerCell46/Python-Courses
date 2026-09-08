import time


class NotInteger(Exception):
    pass


print("First task")

try:
    input_number = int(input("Enter a number or an Error will be thrown: "))
    if type(input_number) != int:
        raise TypeError
except (TypeError, ValueError):
    print(f'You entered an invalid number and an Error was thrown!')


time.sleep(2)
print("Second Task")

try:
    second_task_number = int(input("Enter a number for the second task: "))
    if type(second_task_number) != int:
        raise TypeError
except (TypeError, ValueError):
    print(f'The number that you entered for the second task was invalid and an Error was thrown!')
finally:
    time.sleep(1)
    print(f'The entering phase ended.')


time.sleep(2)
print('Third task')

try:
    third_task_number = int(input("Enter a number for the third task: "))
    if type(third_task_number) != int:
        raise NotInteger
except (NotInteger, ValueError):
    time.sleep(1)
    print("The input data is not an integer!")

time.sleep(2)
print(f'Fourth task')
time.sleep(1)

class GymPRs:
    def __init__(self, name,  squat, deadlift, bench):
        self.name = name
        self.squat = squat
        self.deadlift = deadlift
        self.bench = bench

    def flex(self):
        print(f'{self.name} says: "Yoo bro, my PRs are - deadlift: {self.deadlift}kg, benchpress: {self.bench}kg, squat: {self.squat}kg"')

    def oneThousandPound(self):
        total_weight = self.squat + self.deadlift + self.bench
        total_weight_kg = total_weight * 0.45359237
        if total_weight_kg >= 453.592:
            print("Bro is in the 1000 pound club!")
        else:
            remaining_weight_lb = round(1000 - (total_weight * 2.20462), 1)
            print(f"Worthy for the 1000 pound club?\nYou have to train more! You need {remaining_weight_lb}lbs more to reach the club.")


my_Prs = GymPRs("Peter", 110, 202, 100)
my_Prs.flex()
my_Prs.oneThousandPound()

the_data_is_valid = True
try:
    trainee_name = input("Enter your name: ")
    if type(trainee_name) != str:
        raise ValueError
except ValueError:
    print(f'The name that you entered is not a string, and the program rose an Error!')
    the_data_is_valid = False

try:
    trainee_squat = int(input("Enter your squat PR: "))
    if type(trainee_squat) != int:
        raise ValueError
except ValueError:
    print(f'The squat PR that you entered is not valid and the program rose an Error!')
    the_data_is_valid = False

try:
    trainee_deadlift = int(input("Enter your deadlift PR: "))
    if type(trainee_deadlift) != int:
        raise ValueError
except ValueError:
    print(f'The deadlift PR that you entered is not valid and the program rose an Error!')
    the_data_is_valid = False

try:
    trainee_benchpress = int(input("Enter your benchpress PR: "))
    if type(trainee_benchpress) != int:
        raise ValueError
except ValueError:
    print(f'The benchpress PR that you entered is not valid and the program rose an Error!')
    the_data_is_valid = False

if the_data_is_valid:
    time.sleep(1)
    trainee_Prs = GymPRs(trainee_name, trainee_squat, trainee_deadlift, trainee_benchpress)
    time.sleep(1)
    trainee_Prs.flex()
    time.sleep(1)
    trainee_Prs.oneThousandPound()
else:
    print(f'The class could not be called because you entered invalid data. Sorry.')
