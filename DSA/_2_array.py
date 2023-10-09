# Array ---> List

# it accepts heterogenous data 
# it does not have a fix size
# it is use to store collection of same/different types of data
# fetch the data
# delete the data
# insert the data
# insert the data at a specific position

# lst = [6,7,3,2,5,4]
# lst.append(19)
# lst.extend([1,3,4])
# lst.insert(2,10)
# lst.remove(3)

# print(lst)

class array:
    def __init__(self,fix_size):
        self.fix_size = fix_size
        self.lst = []

    def add(self, element):
        if len(self.lst) < self.fix_size:
            self.lst.append(element)
        else:
            print("Array is Full!")

    def get(self):
        return self.lst

    def pop_element(self, index):
        if index < len(self.lst):
            self.lst.pop(index)
        else:
            print("Index out of range")

arr = array(3)
arr.add(8)
arr.add(7)
arr.add(2)

data = arr.get()
print(data)

arr.remove(1)

data = arr.get()
print(data)