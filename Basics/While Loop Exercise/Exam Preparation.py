number_of_bad_grades = int(input())
task_name = str(input())
grade = int(input())
bad_grades_counter = 0

sum_grades = 0
number_of_tasks = 0
last_task_name = "" \
                 ""
while task_name != "Enough" and bad_grades_counter != number_of_bad_grades:
    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == number_of_bad_grades:
            break
    sum_grades += grade
    number_of_tasks += 1
    last_task_name = task_name
    task_name = str(input())
    if task_name == "Enough":
        break
    grade = int(input())

if task_name == "Enough":
    average_score = sum_grades / number_of_tasks
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {number_of_tasks}')
    print(f'Last problem: {last_task_name}')
elif bad_grades_counter == number_of_bad_grades:

    print(f'You need a break, {bad_grades_counter} poor grades.')
