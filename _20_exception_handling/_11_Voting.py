from _12_customize_exception import InvalidAgeError

class vote:
    def voting(self):
        age = int(input("Enter your age : "))
        if age >= 18:
            print("You voted successfully")
        else:
            try:
                raise InvalidAgeError()
            except Exception as ex:
                print(ex)
        
obj = vote()
obj.voting()

# OOP 
# ATM Project
# pin  

# # pin - digits
#       - length - 4
#       - should not start with 0

1. Deposit
2. Withdraw
3. Mini-Statement