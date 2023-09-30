class book:
    def __init__(self,bookId,bookName,bookAuthor,bookedition,bookPublisher,bookPrice):
        self.bookId =bookId
        self.bookName =bookName
        self.bookAuthor =bookAuthor
        self.bookedition =bookedition
        self.bookPublisher =bookPublisher
        self.bookPrice =bookPrice

    def __str__(self):
        return f"bookid: {self.bookId} \n bookName: {self.bookName} \n bookAuthor: {self.bookAuthor} \n bookedition: {self.bookedition} \n bookPublisher: {self.bookPublisher} \n bookPrice: {self.bookPrice}"

    def get_bookId (self):
        return self.bookId
    
    def get_name (self):
        return self.bookName
    
    def get_author (self):
        return self.bookAuthor
    
    def get_edition (self):
        return self.bookedition
    
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

    def set_edition (self,bookedition):
        self.bookedition =bookedition

    def set_publisher (self,bookPublisher):
        self.bookPublisher =bookPublisher

    def set_price (self,bookPrice):
        self.bookPrice =bookPrice  
