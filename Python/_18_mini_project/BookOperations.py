import random
from Book import book

class bookOperations:
    booklist = []
    def addBook(self):
        print("*******Add Book******")
        num_books = int(input("How many books do you want to add? "))
        for i in range(num_books):
            bookID = random.randint(100, 200)
            bookName = input("Enter book name: ")
            bookAuthor = input("Enter book author name: ")
            bookEdition = input("Enter book edition: ")
            bookPublisher = input("Enter book publisher: ")
            bookPrice = float(input("Enter book price: "))
            book_obj = book(bookID, bookName, bookAuthor, bookEdition, bookPublisher, bookPrice)
            bookOperations.booklist.append(book_obj)
            print("Successfully Added! \n")
        
    def getBook(self):
        print("******Get Book*****",end="\n\n")
        testbook=input("Enter book name to search:-")
        for book in bookOperations.booklist:
            if book.get_name().lower()==testbook.lower():
                print ("***Book Found*****\n",book)
                break
        else:
            print("Book not found")

    def deleteBook(self):
        print("*******Delete Book******")
        book_id = int(input("Enter book id: "))
        for book in bookOperations.booklist:
            if book.get_bookId() == book_id:
                bookOperations.booklist.remove(book)
                print("Book deleted successfully!")
                break
        else:
            print("Book not found!")

    def updateBook(self):
        print("******Update Book*****")
        updateBook=int(input("Enter book Id to update :-"))
        for book in bookOperations.booklist:
            if book.get_bookId()==updateBook:
                bookName = input("Enter book name : ")
                bookAuthor = input("Enter book author name : ")
                bookEdition = input("Enter book edition : ")
                bookPublisher = input("Enter book publisher : ")
                bookPrice = float(input("Enter book price : "))

                book.set_name(bookName)
                book.set_author(bookAuthor)
                book.set_editor(bookEdition)
                book.set_publisher(bookPublisher)
                book.set_price(bookPrice)
                print("Successfully Updated!")
                break
        else:
            print ("\n Book not found!!")

    def viewAllBooks(self):
        print("*******All Books******")
        for book in bookOperations.booklist:
            print(book,"\n")
