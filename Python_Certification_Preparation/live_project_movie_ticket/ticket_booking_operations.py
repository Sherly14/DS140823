class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.user_details = {}

    def show_seats(self):
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i == 0:
                    if j == 0:
                        print(" ",end=" ")
                    else :
                        print(j, end=" ")
                elif j == 0:
                    print(i, end=" ")
                else:
                    print("S", end = " ")
            
            print()

    def buy_ticket(self):
        row = int(input('Enter row number : '))
        col = int(input('Enter the column number : '))
        # for data in self.details:
        #     if data['row'] == row and data['column'] == col:
        #         print("This seat is already booked. Please choose another seat.")
        #         return False
        price=10
        # if self.rows*self.columns>60:
        #     if row >=self.rows/2:
        #         price=8
        ch=int(input(f'Price of the ticket is Rs.{price}. Please press 1 to Confirm or press 0 to Cancel : \n'))
        if ch == 1:
            name=input('Enter your Name : ')
            gender=input('Enter your Gender : ')
            age=int(input('Enter your Age : '))
            phno=int(input('Enter your Phone Number : '))
            seat_no = str(row) + str(col)
            self.user_details[seat_no] = {'name':name,'gender':gender,'age':age,'phoneno':phno,'price':price}
            # self.price+=price
            print("Booked Successfully")
        else:
            print("No Problem! Thank You for connecting with Book My Show!")
            return

    def statistics(self):
        pass

    def user_info(self):
        pass
        