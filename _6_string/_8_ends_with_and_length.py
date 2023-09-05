# 1st Way
l_list = ["ac", "aeroplane","car","bike","laptop","Apple","mango"]
for i in l_list:
    if i[0].lower()=="a" and len(i)>=5:
        print(i)







# 2nd Way
lst=["ac","Aeroplane","car","bike","laptop","apple","mango"]
for i in lst:
    if len(i)>=5 and i.lower().startswith("a"):
        print(i)

