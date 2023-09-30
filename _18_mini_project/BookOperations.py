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
        print("*******Get Book******",end="\n\n")
        testbook=input("Enter book name to search:-")
        for book in bookOperations.booklist:
            if book.get_name().lower()==testbook.lower():
                print ("****Book Found******\n")
                print(f"1)Book name:- {book.get_name()}\n2)Book Number:- {book.get_bookId()}\n3)Author name:- {book.get_author()}\n4)Edition:- {book.get_editor()}\n5)Publisher:- {book.get_publisher()}\n6)Price:- {book.get_price()}\n")
                return book
            else:
                print ("Book not found")
        

    def deleteBook(self):
        print("*******Delete Book******")
        delbook=input("Enter book name to search:-")
        for book in bookOperations.booklist:
            if book.get_name().lower()==delbook.lower():
                print ("****Book Found******\n")
                bookOperations.booklist.remove(book)
                print(f"\nBook with id {book.get_bookId()} is deleted Successfully")
            else:
                print ("\n Book not found!!")
        


    def updateBook(self):
        print("*******Update Book******")
        book=self.getBook()
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
        

    def viewAllBooks(self):
        print("*******All Books******\n")
        ctr=0
        for book in bookOperations.booklist:
            ctr+=1
            print(f'-----{ctr}th book(s)-----')
            print(f"1)Book name:- {book.get_name()}\n2)Book Number:- {book.get_bookId()}\n3)Author name:- {book.get_author()}\n4)Edition:- {book.get_editor()}\n5)Publisher:- {book.get_publisher()}\n6)Price:- {book.get_price()}\n\n")
            
