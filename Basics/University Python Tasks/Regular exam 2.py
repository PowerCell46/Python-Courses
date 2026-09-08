import time


def validate_email(email):
    if email.count("@") == 1:
        at_sign_index = email.index("@")
        if email.count(".") == 1:
            point_index = email.index(".")
            if point_index - at_sign_index > 2:
                if email[-4] == "." or email[-3] == ".":
                    email_list = list(email)
                    email_list.pop(at_sign_index)
                    email_list.pop(point_index - 1)
                    func_result = True
                    for letter in email_list:
                        if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                            func_result = True
                        else:
                            func_result = False
                            break
                    if func_result:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


input_email = str(input("Enter an email that you wish to validate: "))
time.sleep(3)
result = validate_email(input_email)
print(f'The syntax of the email that you have entered is: {result}')

time.sleep(1)
print("---------------------")
print("Second task")
time.sleep(2)

set_of_emails = set(["ivan@abv.bg", "ivan@me.com", "ivan@gmail.com", "ivan@a.bg", "ivan@.com", "ivan@gmail.m", "ivan@@gmail.com", "ivan_gmail.com", "иван@гмайл.цом"])
list_of_emails = list(set_of_emails)
print(f'This is the list of emails that we have to validate: {", ".join(list_of_emails)}')

time.sleep(3)
valid_emails = list(filter(lambda x: (validate_email(x) == True), list_of_emails))
print(f'Using filter and lambda we leave out only the valid emails from the list: {", ".join(sorted(valid_emails, key= lambda x: x))}')

valid_emails_2 = list(map(validate_email, list_of_emails))
map_valid_emails = []
for i in range(len(list_of_emails)):
    if valid_emails_2[i]:
        map_valid_emails.append(list_of_emails[i])
time.sleep(3)
print(f'Using map we get if the email is valid or not, resulting in a boolean answer. Using a for cycle we determine which of the emails are valid: {", ".join(map_valid_emails)}')

print("---------------------")
