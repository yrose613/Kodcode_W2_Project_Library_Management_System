from functions import display_books, search_book, add_book, borrow_book, return_book, get_available_books, get_books_by_author, get_next_book_id

from data import books

def main():
    user_input = ""
    while user_input != "8":
        print("""\n================================
        1. Display all books
        2. Search book by name
        3. Add new book
        4. Borrow a book
        5. Return a book
        6. Display available books
        7. Display books by author
        8. Exit)
        """)
        user_input = input("Choose an option: ")

        display_books, search_book, add_book, borrow_book, return_book, get_available_books, get_books_by_author, get_next_book_id

        if user_input == "1":
            print("You've selected option 1")
        elif user_input == "2":
            print("You've selected option 2")
        elif user_input == "3":
            print("You've selected option 3")
        elif user_input == "4":
            print("You've selected option 4")
        elif user_input == "5":
            print("You've selected option 5")
        elif user_input == "6":
            print("You've selected option 6")
        elif user_input == "7":
            print("You've selected option 7")
        elif user_input == "8":
            print("Bye Bye!")
        else:
            print("Invalid input, try again")

main()