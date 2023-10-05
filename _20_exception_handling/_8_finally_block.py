try:
    print(10/0)
except Exception as ex:
    print(ex)
finally:
    print("Finally part")

# finally block will execute everytime regardless if whether exception has occured or not
# it is mainly use to close the file and close the database
