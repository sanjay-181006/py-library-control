class Book:
    def __init__(self, book_id, title, author, total_copies, available_copies):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.__total_copies=total_copies
        self.__available_copies=available_copies
    def borrow_book(self):
        if self.__available_copies==0:
            return "Book not available"
        else:
            self.__available_copies-=1
            
            return "Successfully borrowed"
    def return_book(self):
        self.__available_copies+=1
        if self.__total_copies<self.__available_copies:
            return "Try Again!!" 
        else:
            return "Successfully Returned"
    def get_available_copies(self):
        return self.__available_copies
    def __str__(self):
        return f"Book id={self.book_id}, Title={self.title}, Author={self.author}, Total Copies={self.__total_copies}, Available Copies={self.__available_copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id=member_id
        self.__borrowed_books=[]   
        self.name=name
    def borrow(self, book):
        self.__borrowed_books.append(book)    
    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            return "Successfuly Returned"
        else:
            return "Book not borrowed"
    def get_borrowed_books(self):
        return self.__borrowed_books
    def __str__(self):
        return f"Member ID={self.member_id}, Name={self.name}, Books borrowed={self.__borrowed_books}"


class Library:
    def __init__(self):
        self.__books = {}    
        self.__members = {}    
    def add_book(self, book):
        self.__books[book.book_id] = book
    def add_member(self, member):
        self.__members[member.member_id] = member
    def issue_book(self, book_id, member_id):
        if book_id in self.__books and member_id in self.__members:
            book=self.__books[book_id]
            member=self.__members[member_id]
            member.borrow(book)
            return "Book successfully issued"
    def return_book(self, book_id, member_id):
        if book_id not in self.__books:
            return "Book not found"
        if member_id not in self.__members:
            return "Member not found"

        book = self.__books[book_id]
        member = self.__members[member_id]

        if book not in member.get_borrowed_books():
            return "This member did not borrow this book"
        member.return_book(book)
        book.return_book()
        return "Book successfully returned"

    def display_books(self):
        return self.__books
    def display_members(self):
        return self.__members
        
            
      
        
        
    
        
