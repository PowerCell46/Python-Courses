#First Task

first_task_input_number = int(input("Enter a number for the first task: "))
print(f'The result of {first_task_input_number} * {first_task_input_number} is: {first_task_input_number * first_task_input_number}')

def recursion(num, res=1):
    if num > 0:
        res *= num
        num -= 1
        return recursion(num, res)
    else:
        return res
      
print(f'The result of {first_task_input_number} factorial is: {recursion(first_task_input_number)}')

#Second Task

print(f'Hello there, {input("Enter your name: ")}!')

#Third Task
a = 5
b = 10
print(f'a is {a} and b is {b}')
a, b = b, a
print(f'a is {a} and b is {b}')
