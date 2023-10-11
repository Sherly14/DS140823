# Queue

# FIFO - First In First Out

# list
# deque

# from collections import deque

class queue:
    def __init__(self):
        # self.queue_list = deque()
        self.queue_list = []

    def enqueue(self,element):
        self.queue_list.append(element)
        print("Element is added in Queue")

    def dequeue(self):
        if not self.is_empty():
            return self.queue_list.pop(0)
        else:
            print("Empty Queue!")
    
    def get_front(self):
        if not self.is_empty():
            return self.queue_list[0]
        else:
            print("Empty Queue!")

    def get_rear(self):
        if not self.is_empty():
            return self.queue_list[-1]
        else:
            print("Empty Queue!")
    
    def get(self):
        if not self.is_empty():
            return self.queue_list
        else:
            print("Empty Queue!")
     
    def is_empty(self):
        return len(self.queue_list) == 0

    def length(self):
        if not self.is_empty():
            return len(self.queue_list)
        else:
            print("Empty Queue!")

obj = queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)

data = obj.get()
print(data)

obj.dequeue()

data = obj.get()
print(data)

front_value = obj.get_front()
print(front_value)

rear_value = obj.get_rear()
print(rear_value)

isEmpty = obj.is_empty()
print(isEmpty)

q_length = obj.length()
print(q_length)

