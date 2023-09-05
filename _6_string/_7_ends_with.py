# lst = ["sun","cat","mat","cot","sat","rat","run"]

# "cat"
# "mat"
# "sat"
# "rat"





# 1st Way

# lst = ["sun", "cat", "mat","cot","sat", "rat","run"]
# for i in lst:
#     if i[1]=="a" and i[2]=="t":
#         print(i)





# 2nd Way

# list1=["sun","cat","mat","cot","sat","rat","run"]
# for i in range(len(list1)):
#     if "at" in list1[i]:
#         print(list1[i])





# 3rd Way

# lst = ["sun", "cat", "mat","cot","sat", "rat","run"]

# for i in lst:
#     if i.endswith("at"):
#         print(i)





# 4th Way 

# lst=["sun","cat","mat","rat","cot","sat","rat","run"]
# for i in lst:
#     if i in ["cat","mat","rat","sat"]:
#         print(i)






# 5th Way

lst = ["sun", "cat", "mat", "cot", "sat", "rat", "run"]
filtered_lst = []

for word in lst:
    if word[-2:] == "at":
        filtered_lst.append(word)

print(filtered_lst)





# 6th Way 

lst = ["sun", "cat", "mat","cot","sat", "rat","run"]

for i in lst:
    if i[-2]=="a" and i[-1]=="t":
        print(i)


# ["ac","aeroplane","car","bike","laptop","apple","mango"]
