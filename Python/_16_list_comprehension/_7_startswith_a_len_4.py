lst = ["ac","Aeroplane","mango","grapes","apple"]
len_list = [i for i in lst if len(i)>4 and i[0].lower() == 'a']
print(len_list)