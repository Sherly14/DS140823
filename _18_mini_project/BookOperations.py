import random
from Book import book

class bookOperations:
    booklist = []
    def addBook(self):
        print("*******Add Book******")
        bookID = random.randint(100,200)
        bookName = input("Enter book name : ")
        bookAuthor = input("Enter book author name : ")
        bookEdition = input("Enter book edition : ")
        bookPublisher = input("Enter book publisher : ")
        bookPrice = float(input("Enter book price : "))
        book_obj = book(bookID,bookName,bookAuthor,bookEdition,bookPublisher,bookPrice)
        bookOperations.booklist.append(book_obj)
        print("Successfully Added!")
        

    def getBook(self):
        print("*******Get Book******")

    def deleteBook(self):
        print("*******Delete Book******")

    def updateBook(self):
        print("*******Update Book******")

    def viewAllBooks(self):
        print("*******All Books******")
