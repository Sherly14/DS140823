from ticket_booking_operations import movie_ticket

class Main:
    def execute(self,choice):
        if choice == 1:
            print("***************Show the seats******************")
            movie_obj.show_seats()
        elif choice == 2:
            print("***************Buy Ticket******************")
            movie_obj.buy_ticket()
        elif choice == 3:
            print("***************Statistics******************")
            movie_obj.statistics()
        elif choice == 4:
            print("***************User Info******************")
            movie_obj.user_info()
        else:
            print("***************Thank You for connecting with us! Good Bye!******************")

if __name__ == "__main__":
    rows = int(input("Enter the number of rows : "))
    cols = int(input("Enter the number of seats in each rows : "))

    choice = int(input("Enter \n1.Show the seats \n2.Buy a ticket \n3.Statistics \n4.Show booked ticket's user info \n0.Exit : \n"))

    movie_obj = movie_ticket(rows,cols)

    obj = Main()
    obj.execute(choice)

    


    


