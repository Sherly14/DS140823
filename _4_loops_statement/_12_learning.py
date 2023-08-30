num = int(input("Enter number:")) # 123 = 321

reverse = 0

while num != 0 :         
    digit = num % 10       
    print("digit : ",digit)
    reverse = (reverse*10) + digit   
    print("reverse : ",reverse)
    num =  num // 10  
    print("num : ",num)        
           
print(reverse) 