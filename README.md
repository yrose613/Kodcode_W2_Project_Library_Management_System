# Library Management System

A beginner Python project with a text menu for displaying, searching, adding,
borrowing, and returning library books. You can also display available books
or books by author.

Run the program with Python 3:

```text
python main.py
```

Choose an option from 1 to 8 and follow the prompts. Use a whole number for
the publication year or book ID. New books need a name, an author, and a
positive year. A book with the same name and author cannot be added twice.

Name searches accept partial matches and return the first matching book.
Author searches use the full author name. Both ignore letter case.

The program starts with the five books from the project specification.
Changes stay in memory while it runs and reset when it starts again.

- `main.py` runs the menu and collects user input.
- `functions.py` contains the book operations and validation.
- `data.py` creates the starting book list.
