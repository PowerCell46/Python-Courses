right_user = str(input())
right_pass = str(input())

input_pass = str(input())

while input_pass != right_pass:
    input_pass = str(input())


if input_pass == right_pass:
    print(f'Welcome {right_user}!')
