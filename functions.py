# Displays all books
# returns None
def display_books(books):
    if len(books) == 0:
        print("No books found")
    for sub_dict in books:
        print(sub_dict, end="\n")
    print("")


# Searches for a book by name, including partial matches
# returns A book or None
def search_book(books, name):
    name = name.strip()
    if name == "":
        return None

    for sub_dict in books:
        if name.lower() in sub_dict["name"].lower():
            return sub_dict
    return None


# Generates a new ID
# returns int
def get_next_book_id(books):
    highest_id = 0
    for sub_dict in books:
        if sub_dict["id"] > highest_id:
            highest_id = sub_dict["id"]
    return highest_id + 1


# Adds a new book
# returns bool
def add_book(books, name, author, year):
    name = name.strip()
    author = author.strip()
    if name == "" or author == "":
        return False
    if not isinstance(year, int):
        return False
    if year <= 0:
        return False

    for sub_dict in books:
        if name.lower() == sub_dict["name"].lower() and author.lower() == sub_dict["author"].lower():
            return False

    new_book = {
        "id": get_next_book_id(books),
        "name": name,
        "author": author,
        "year": year,
        "available": True
    }
    books.append(new_book)
    return True


# Lends a book and updates its availability
# returns bool
def borrow_book(books, book_id):
    for sub_dict in books:
        if book_id == sub_dict["id"]:
            if sub_dict["available"] == False: # i.e. checks if it's unavailable
                return False
            else:
                sub_dict["available"] = False
                return True
    return False


# Returns a book and updates its availability
# returns bool
def return_book(books, book_id):
    for sub_dict in books:
        if book_id == sub_dict["id"]:
            if sub_dict["available"] == True: # i.e. checks if it's already been returned
                return False
            else:
                sub_dict["available"] = True # i.e. you've returned it
                return True
    return False


# Returns only available books
# returns list
def get_available_books(books):
    available_books = []
    for sub_dict in books:
        if sub_dict["available"] == True:
            available_books.append(sub_dict)

    return available_books


# Searches for books by the author's name
# returns list
def get_books_by_author(books, author):
    author = author.strip()
    books_by_author = []
    for sub_dict in books:
        if sub_dict["author"].lower() == author.lower():
            books_by_author.append(sub_dict)

    return books_by_author
