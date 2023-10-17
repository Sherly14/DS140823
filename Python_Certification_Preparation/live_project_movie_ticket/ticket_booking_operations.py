class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.user_details = {}
        self.income = 0

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

        total_seats = self.rows * self.columns

        if total_seats <= 60:
            price = 10
        else:
            if row <= (self.rows//2):
                price = 10
            else:
                price = 8

        # for data in self.details:
        #     if data['row'] == row and data['column'] == col:
        #         print("This seat is already booked. Please choose another seat.")
        #         return False
        
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
            self.income += price
            print("Booked Successfully")
        else:
            print("No Problem! Thank You for connecting with Book My Show!")
            return

    def statistics(self):
        total_seats = self.rows * self.columns # 9 8
        purchased_ticket = len(self.user_details)
        purchased_tkt_per = (purchased_ticket / total_seats) * 100
        total_income = 0

        if total_seats > 60:
            front_price = 10
            back_price  = 8
            front_seats = (self.rows // 2) * self.columns
            back_seats = total_seats - front_seats
            total_income  = front_seats * front_price + back_seats * back_price

            # temp=(self.rows*self.columns)*10
            # t2=self.rows//2
            # t1=temp-(t2*self.columns)*2
            # total+=t1
        else:
            total_income = total_seats * 10

        print('Number of Purchased Tickets : ',purchased_ticket)
        print('Percentage of Tickets booked',purchased_tkt_per)
        print('Current Income : ',self.income)
        print("Total Income : ",total_income)

    def user_info(self):
        pass
        