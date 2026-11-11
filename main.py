from functions import display_books, search_book, add_book, borrow_book, return_book, get_available_books, get_books_by_author

from data import get_initial_books

def main():
    books = get_initial_books()
    user_input = ""
    while user_input != "8":
        print("""\n================================
        LIBRARY MANAGEMENT
================================
        1. Display all books
        2. Search book by name
        3. Add new book
        4. Borrow a book
        5. Return a book
        6. Display available books
        7. Display books by author
        8. Exit
        """)
        user_input = input("Choose an option: ").strip()

        if user_input == "1":
            display_books(books)
        elif user_input == "2":
            name = input("Enter the book name: ")
            book = search_book(books, name)
            if book == None:
                print("Book not found")
            else:
                print(book)
        elif user_input == "3":
            name = input("Enter the book name: ")
            author = input("Enter the author: ")
            try:
                year = int(input("Enter the publication year: "))
            except ValueError:
                print("The publication year must be a positive whole number")
                continue

            if add_book(books, name, author, year):
                print("Book added successfully")
            else:
                print("Book not added. Name and author are required, year must be positive, and the book must not already exist")
        elif user_input == "4":
            try:
                book_id = int(input("Enter the book ID: "))
            except ValueError:
                print("The book ID must be a whole number")
                continue

            if borrow_book(books, book_id):
                print("Book borrowed successfully")
            else:
                print("Book not found or already on loan")
        elif user_input == "5":
            try:
                book_id = int(input("Enter the book ID: "))
            except ValueError:
                print("The book ID must be a whole number")
                continue

            if return_book(books, book_id):
                print("Book returned successfully")
            else:
                print("Book not found or already in the library")
        elif user_input == "6":
            available_books = get_available_books(books)
            display_books(available_books)
        elif user_input == "7":
            author = input("Enter the author: ")
            books_by_author = get_books_by_author(books, author)
            display_books(books_by_author)
        elif user_input == "8":
            print("Bye Bye!")
        else:
            print("Invalid input, try again")

if __name__ == "__main__":
    main()
