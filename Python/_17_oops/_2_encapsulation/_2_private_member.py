# __ allows you to make your variable private, which will not get modified outside the class

username = "vaibhavi"
class encapsulation:

    def __init__(self):
        self.__name = "Bharati"

    def set_name(self,name):
        if username == "vaibhavi":
            self.__name = name

    def get_name(self):
        if username == "vaibhavi":
            return self.__name

obj = encapsulation()

# print(obj.__name)
print(obj.get_name())

obj.set_name("Shruti")

print(obj.get_name())

# obj.a = "abc"
# print(obj.a)

# obj.__name = "Shruti"
# print(obj.__name)

