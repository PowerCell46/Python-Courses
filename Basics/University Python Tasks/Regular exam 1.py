# факултетен номер: 3GG0800040
bulgarian_input_text = str(input())
bulgarian_input_text = bulgarian_input_text.split(" ")

final_bulgarian_text_string = ""
vowels_counter = 0
incorrect_symbols = []

for word in bulgarian_input_text:
    for letter in word:
        if 1040 <= ord(letter) < 1072 or 1071 < ord(letter) <= 1103:
            final_bulgarian_text_string += letter
            if letter == "а" or letter == "ъ" or letter == "о" or letter == "y" or letter == "е" or letter == "и":
                vowels_counter += 1
else:
            incorrect_symbols.append(letter)
    final_bulgarian_text_string += " "

incorrect_symbols = set(incorrect_symbols)
incorrect_symbols = list(incorrect_symbols)

print(f'Брой на гласните букви: {vowels_counter}')
print(f'Преработеният стринг е следният: {final_bulgarian_text_string}')
print(f'Невалидните символи са: {" ".join(incorrect_symbols)}')
