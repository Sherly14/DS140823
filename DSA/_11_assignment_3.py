class string():
    def __init__(self):
        self.string1 = ""
        self.string2 = ""

    def input_strings(self):
        self.string1 = input("Enter the first string: ")
        self.string2 = input("Enter the second string: ")
       
    def are_rotations(self):
        if len(self.string1) != len(self.string2):
            return False
        
        str1_str2 = self.string1 + self.string1
        print(self.string1,self.string2,str1_str2)
        if self.string2 in str1_str2:
            print("The strings are rotations of each other.")
        else:
            print("The strings are not rotations of each other.")

obj = string()


obj.input_strings()
obj.are_rotations()