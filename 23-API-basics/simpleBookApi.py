# SimpleBookAPI

class Bookstore:
    def __init__(self):
        self.books = []
        pass

    def add_book(self,id,title,author,year,genre):
        new_book = {
            'id': id,
            'title': title,
            'author': author,
            'year':year,
            'genre':genre
        }
        self.books.append(new_book)
        return new_book

    def get_book_by_id(self,id):
        for book in self.books:
            if book.get("id") == id:
                print(book.get("title"))
                return book
        else:
            print("No such book available")
            return None

if __name__ == "__main__":
    bookstore = Bookstore()

    book1 = bookstore.add_book(1,"The Lord of the rings","J.R.R. Tolkien","1954","fantasy novel")
    book2 = bookstore.add_book(2,"Pride and Prejudice","Jane Austen","1813","Romance novel")

    bookstore.get_book_by_id(1)
    bookstore.get_book_by_id(2)
    bookstore.get_book_by_id(3)
    