class book:
    def __init__(self,bookId,bookName,bookAuthor,bookEditor,bookPublisher,bookPrice):
        self.bookId =bookId
        self.bookName =bookName
        self.bookAuthor =bookAuthor
        self.bookEditor =bookEditor
        self.bookPublisher =bookPublisher
        self.bookPrice =bookPrice

    def __str__(self):
        return f"Book ID: {self.bookId} \nBook Name: {self.bookName} \nBook Author: {self.bookAuthor} \nBook Editor: {self.bookEditor} \nBook Publisher: {self.bookPublisher} \nBook Price: {self.bookPrice}"

    def get_bookId (self):
        return self.bookId
    
    def get_name (self):
        return self.bookName
    
    def get_author (self):
        return self.bookAuthor
    
    def get_editor (self):
        return self.bookEditor
    
    def get_publisher (self):
        return self.bookPublisher
    
    def get_price (self):
        return self.bookPrice
    
    def set_bookId (self,bookId):
        self.bookId =bookId

    def set_name (self,bookName):
        self.bookName =bookName 

    def set_author (self,bookAuthor):
        self.bookAuthor =bookAuthor

    def set_editor (self,bookEditor):
        self.bookEditor =bookEditor

    def set_publisher (self,bookPublisher):
        self.bookPublisher =bookPublisher

    def set_price (self,bookPrice):
        self.bookPrice =bookPrice  
        