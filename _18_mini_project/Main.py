from BookOperations import *

try:

    class main:
        def execute(self,choice,operation):
            if choice == 1:
                operation.addBook()
            elif choice == 2:
                operation.getBook()
            elif choice == 3:
                operation.deleteBook()
            elif choice == 4:
                operation.updateBook()
            elif choice == 5:
                operation.viewAllBooks()
            else:
                exit(1)

    global obj ;obj=main()
    operation = bookOperations()

    while True:
        choice = int(input("Enter \n1.Add Book \n2.Find Book \n3.Delete Book \n4.Update Book \n5.View All Books \n6.Exit: \n"))
        obj.execute(choice,operation)

except:
    print("wrong detail")
    
    while True:
        choice = int(input("Enter \n1.Add Book \n2.Find Book \n3.Delete Book \n4.Update Book \n5.View All Books \n6.Exit: \n"))
        obj.execute(choice,operation)
1