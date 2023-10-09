# email from user
# bharati@yahoo.com            - yahoo
# bharati@gmail.com            - gmail
# bharati@edyoda.com           - edyoda
# bharati@rediffmail.com       - rediffmail

# mail=input("enter mail")
# i=mail.find("@") # 6
# j=mail.find(".") # 10
# domain=mail[i+1:j]
# print(domain)

email = input("Enter email:")
print(email[(email.find("@")+1):email.find(".")]) 


