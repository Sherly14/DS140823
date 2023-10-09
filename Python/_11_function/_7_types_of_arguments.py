# Types of argument/paramters

# 1. required/positional argument
# 2. default argument
# 3. keyword argument
# 4. variable-length argument
#    4.1. Arbitary positional argument
#    4.2. Arbitary keyword argument


# 1. required/positional argument
# def student(rno,name):
#     print(f"Rno : {rno} and Name : {name}")

# student(1,"Bharati")





# 2. default argument
# def student(address,rno=10,name="Pranay"):
#     print(f"Rno : {rno} and Name : {name} and Address : {address}")

# student("Mumbai",12,"Rahees")





# 3. keyword argument
# def student(address,rno=10,name="Pranay"):
#     print(f"Rno : {rno} and Name : {name} and Address : {address}")

# student(address="Mumbai",name="Bharati")





# 4. variable-length argument
#    4.1. Arbitary positional argument
# *args
# tuple

# def users(*args):
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)
#     args_lst = list(args)
#     print(args_lst,type(args_lst))
#     print(args_lst[4])

# users(1,2,3,4,"Vinay","Subha","Vinu")





# 4. variable-length argument
#    4.2. Arbitary keyword argument
# **kwargs
# dict

def users(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["two"])

users(one="Bharati",two="Vinu",three="Abhi",four="Avi")




