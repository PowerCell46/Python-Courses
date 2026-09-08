target_book = str(input())
current_book = str(input())
books_counter = 0

while current_book != target_book and current_book != "No More Books":
    books_counter += 1
    current_book = str(input())

if current_book == target_book:
    print(f'You checked {books_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_counter} books.')
