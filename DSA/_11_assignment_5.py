# string="malayalam"
string= input("Enter string : ")
def palindrome(string):
    if len(string)==1:
        return True
    if string[0]==string[-1]:
        print(string[1:-1])
        return palindrome(string[1:-1])
    else:
        return False
print(palindrome(string))

string = "edyoda"
string[1:-1]