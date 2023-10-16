class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns

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

        # print("\nCinema:")
        # print("  " + " ".join(map(str, range(1, self.seats_per_row + 1))))
        # for i, row in enumerate(self.seating_plan, start=1):
        #     print(f"{i} {' '.join(['S' if seat == 1 else 'S' for seat in row])}")

    def buy_ticket(self):
        pass

    def statistics(self):
        pass

    def user_info(self):
        pass
        