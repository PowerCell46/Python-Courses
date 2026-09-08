number_of_open_tabs = int(input())
salary = int(input())
taken_money = 0
salary_lost = False

for index in range(0, number_of_open_tabs):
    current_tab = str(input())
    if current_tab == "Facebook":
        salary -= 150
    elif current_tab == "Instagram":
        salary -= 100
    elif current_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        salary_lost = True
        break


if salary_lost == False:
    print(salary)
