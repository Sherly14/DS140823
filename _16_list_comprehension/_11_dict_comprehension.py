# dict comprehension - is use to create new dict 

str1 = "Python"
# o/p : {'P':'p','Y':'y'......}

dict_com = {i.upper():i.lower() for i in str1}
print(dict_com)


keys = [1,2,3,4,5]
values = [10,20,30,40,50]
o/p : {1:10,2:20,3:30,4:40,5:50}