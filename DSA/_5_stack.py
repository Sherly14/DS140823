# STACK - LIFO - Last in first out
# list
# deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)


topele = stack.pop()
print("Popped element:", topele) 

peekele = stack.peek()
print("Top element:", peekele)   


print(stack.get_stack())

print(stack.is_empty())

stack.clearAll()

print(stack.is_empty())
