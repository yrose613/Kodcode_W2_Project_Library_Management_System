books = [
    {
        "id": 1,
        "name": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "available": True
    },
    {
        "id": 2,
        "name": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "year": 1998,
        "available": True
    },
    {
        "id": 3,
        "name": "Harry Potter and the Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "year": 1999,
        "available": False
    },
    {
        "id": 4,
        "name": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "year": 2000,
        "available": True
    },
    {
        "id": 5,
        "name": "Harry Potter and the Order of the Phoenix",
        "author": "J.K. Rowling",
        "year": 2003,
        "available": False
    },
    {
        "id": 6,
        "name": "Harry Potter and the Half-Blood Prince",
        "author": "J.K. Rowling",
        "year": 2005,
        "available": True
    },
    {
        "id": 7,
        "name": "Harry Potter and the Deathly Hallows",
        "author": "J.K. Rowling",
        "year": 2007,
        "available": True
    },
    {
        "id": 8,
        "name": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "available": True
    },
    {
        "id": 9,
        "name": "The Fellowship of the Ring",
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "available": True
    },
    {
        "id": 10,
        "name": "The Two Towers",
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "available": False
    },
    {
        "id": 11,
        "name": "The Return of the King",
        "author": "J.R.R. Tolkien",
        "year": 1955,
        "available": True
    },
    {
        "id": 12,
        "name": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": False
    },
    {
        "id": 13,
        "name": "Atomic Habits",
        "author": "James Clear",
        "year": 2018,
        "available": True
    },
    {
        "id": 14,
        "name": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "year": 1999,
        "available": False
    }
]


# Displays all books
# returns None
def display_books(books):
    for sub_dict in books:
        print(sub_dict, end="\n")
    print("")
    
# display_books(books)

# Searches for a book by name, including partial matches
# returns A book or None
def search_book(books, name):
    for sub_dict in books:
        if name.lower() in sub_dict["name"].lower(): # Reminder, what's in the [] must be the name of the 
            print(sub_dict)
            # return True

search_book(books, "Harry")


# search_book(books, "Harry Potter")

# Adds a new book
# returns bool
def add_book(books, name, author, year):
    new_book = {
        "id": 5,
        "name": name.strip(),
        "author": author.strip(),
        "year": year,
        "available": True
    }
    books.append(new_book)

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

# print(borrow_book(books, 3))
# print(borrow_book(books, 4))

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

# print(return_book(books, 3))
# print(return_book(books, 4))

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
    list_of_authors = []
    for sub_dict in books:
        if sub_dict["author"] == author:
            available_books.append(sub_dict)

# Generates a new ID
# returns int
def get_next_book_id(books):
    pass



# def close_the_order(DB):
#     user_select = int(input("Which order would you like to close: "))


#     for sub_dict in DB:
#         if user_select == sub_dict["id"]:
#             if sub_dict["status"] == "CLOSED":
#                 print("\nThe order you've selected has already been closed")
#             else:
#                 sub_dict["status"] = "CLOSED"

#     for sub_dict in DB:
#         print(sub_dict, "\n")

# display_books(books)

# print(books[0].get("author"))
# try:
#     if 
# print(books[0].get("random_key"), 0)

"""
for sub_dict in books:
    for key in sub_dict: # Note: key can be any variable
        print(sub_dict[key]) # The thing to note is that once you want to access the key's value, you need to do dict[key] i.e. key in square bracket

"""

# ANY TIME YOU DO NOT HAVE dict[key] YOU ARE DEALING WITH THE DICTIONARY AS IF IT WAS A LIST OF IDs
# AND YOU CAN DO ALL THE REGULAR THINGS DO THE DICT THAT YOU CAN DO TO A LIST