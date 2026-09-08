input_word = str(input())
sum = 0

for current_index in range(0, len(input_word)):
    current_symbol = input_word[current_index]
    if current_symbol == "a":
        sum += 1
    elif current_symbol == "e":
        sum += 2
    elif current_symbol == "i":
        sum += 3
    elif current_symbol == "o":
        sum += 4
    elif current_symbol == "u":
        sum += 5

print(sum)
