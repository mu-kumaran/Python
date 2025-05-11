# Simple library application
from simpleBookApi import Bookstore

class LibraryManagement:
    def __init__(self,bookstore):
        self.bookstore = bookstore

    def add_books(self,id,title,author,year,genre):
        new_book = self.bookstore.add_book(id,title,author,year,genre)
        return new_book



if __name__ == "__main__":

    # Directly using simplebook API
    bookstore = Bookstore()
    bookstore.add_book(1,"The Handmaid's Tale","Margaret Atwood","1985","Science Fiction")
    bookstore.add_book(2,"To Kill a Mockingbird","Harper Lee","1960","Historical Fiction")
    bookstore.get_book_by_id(1)
    bookstore.get_book_by_id(2)
    print(bookstore.books)

    # Passing simpleBook API to libraryManagement class
    new_bookstore = Bookstore()
    lib = LibraryManagement(new_bookstore)
    lib.add_books(1,"Hitchhiker's Guide to the Galaxy","Douglas Adams","1979","Science Fiction")
    new_bookstore.get_book_by_id(1)
    new_bookstore.get_book_by_id(2)
    print(new_bookstore.books)