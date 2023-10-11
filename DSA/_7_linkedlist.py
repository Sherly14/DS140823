class node:
    def __init__(self,data,link):
        self.data = data
        self.link = link


class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def append(self,data):
        new_node = node(data,self.head) # data = 10, link = None
        self.head = new_node            # data = 10, link = None

    def display(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.link

obj = linkedlist()
obj.append(10)
obj.append(20)

obj.display()