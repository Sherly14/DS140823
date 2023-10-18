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
                    seat_no = str(i) + str(j)
                    if seat_no in self.user_details:
                        print("B", end=" ")
                    else:
                        print("S", end=" ")
            print()

    # def show_seats(self):
    #     print("  " + " ".join(map(str, range(1, self.seats_per_row + 1))))
    #     for row_number, row in enumerate(self.seating_plan, start=1):
    #         print(f"{row_number} {' '.join(row)}")

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

        ch=int(input(f'Price of the ticket is Rs.{price}. Please press 1 to Confirm or press 0 to Cancel : \n'))
        if ch == 1:
            name=input('Enter your Name : ')
            gender=input('Enter your Gender : ')
            age=int(input('Enter your Age : '))
            phno=int(input('Enter your Phone Number : ')) # 320 + 320
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
        else:
            total_income = total_seats * 10

        print('Number of Purchased Tickets : ',purchased_ticket)
        print('Percentage of Tickets booked',purchased_tkt_per)
        print('Current Income : ',self.income)
        print("Total Income : ",total_income)

    def user_info(self):
        row,column=map(int,input("Please Enter the row and column : ").split(","))
        seat_no=str(row)+str(column)

        if seat_no in self.user_details:
            user_data = self.user_details[seat_no]
            print(f"Name : {user_data['name']}")
            print(f"Gender : {user_data['gender']}")
            print(f"Age : {user_data['age']}")
            print(f"TicketPrice : {user_data['price']}")
            print(f"PhoneNumber : {user_data['phoneno']}")
        else:
            print("The seat you have chosen not occupied by anyone")
        

# CRUD - Create, Read, Update, Delete