def dict_sort():
    dict1={}
    size=int(input("Enter the size of the dictionary "))
    for i in range(size):
        key=int(input("Enter the key element "))
        val=int(input("Enter the value "))
        dict1[key]=val
    print("The dictionary created is",dict1)

    dict2={}
    l1=list(dict1.keys())
    print(l1) # [5,6,1]
    l1.sort()
    print(l1) # [1,5,6]

    for i in l1:
        dict2[i]=dict1[i]

    print("The sorted dictionary is",dict2)
    
dict_sort()