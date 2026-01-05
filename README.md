# Library Management System (Python OOP)

This project is a Library Management System implemented using Python Object-Oriented Programming (OOP) principles.  
It simulates real-world library operations such as adding books, registering members, issuing books, and returning books, while maintaining proper data encapsulation and class responsibility.

---

## Features

- Add and manage books in the library
- Register library members
- Issue books to members
- Return books with validation
- Track available copies of books
- Track books borrowed by each member
- Clean separation of responsibilities using OOP

---

## OOP Design Overview

The system is built using three main classes:

### Book
Handles book-related data and availability.

Attributes:
- book_id
- title
- author
- __total_copies (private)
- __available_copies (private)

Responsibilities:
- Borrow a book
- Return a book
- Track available copies

---

### Member
Represents a library member.

Attributes:
- member_id
- name
- __borrowed_books (private)

Responsibilities:
- Borrow books
- Return books
- Track borrowed books

---

### Library
Acts as the controller that coordinates interactions between books and members.

Attributes:
- __books (private dictionary)
- __members (private dictionary)

Responsibilities:
- Add books
- Add members
- Issue books
- Return books
- Display books and members

---

## Technologies Used

- Language: Python 3
- Programming Topic: Object-Oriented Programming (OOP)

---

## Sample Usage

```python
library = Library()

book1 = Book(101, "1984", "George Orwell", 5, 5)
member1 = Member(1, "Alice")

library.add_book(book1)
library.add_member(member1)

print(library.issue_book(101, 1))
print(library.return_book(101, 1))

