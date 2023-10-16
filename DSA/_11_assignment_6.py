# string = input("Enter the postfix : ")

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)  

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return None
      
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]  
#         else:
#             return None
    
#     def get_stack(self):
#         if not self.is_empty():
#             return self.items
#         else:
#             return None
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def clearAll(self):
#         self.items.clear()
#         print("All Elements removed.")


# def postfix(string):
#     res=''
#     if len(string)<=1:
#         return string
#     else:
#         stack=Stack()
#         for strs in string:
#             if strs in ["+",'-','*','/']:
#                 s1=stack.peek()
#                 stack.pop()
#                 s2=stack.peek()
                
#                 stack.pop()
#                 try:
#                     res=strs+s2+s1+res
#                 except:
#                     print ('Enter the valid postfix : ')
#             else:
#                 stack.push(strs)
#     return res
# print('Prefix : ',postfix(string))
# """
# -----Expected Output-----
# Enter the postfix : 56-23+
# Prefix :  +23-56
# """


def postfix_to_prefix(post):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for opr in post.split():
        if opr not in operators:
            stack.append(opr)
        else:
            var2 = stack.pop()
            var1 = stack.pop()
            pre = opr + var1 + var2
            stack.append(pre)

    return stack[0]

post = input("Enter a postfix expression separated by spaces: ")
pre = postfix_to_prefix(post)
print("Th Prefix expression is:", pre)