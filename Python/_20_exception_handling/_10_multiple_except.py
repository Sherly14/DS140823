try:
    print(10/0)
except TypeError as ex:
    print("TypeError")
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
except SyntaxError as ex:
    print("SyntaxError")
except Exception as ex:
    print("Exception")