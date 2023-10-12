class node:
    def __init__(self,data,link):
        self.data = data
        self.link = link

class linkedlist:
    def __init__(self,head=None):
        self.head = head
        self.ctr = 0

    def append(self,data):
        new_node = node(data,self.head) # data = 10, link = None
        self.head = new_node            # data = 10, link = None || data = 20
        self.ctr += 1 

    def display(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.link
        
    def is_empty(self):
        return self.head == None
    
    def length(self):
        return self.ctr
    
    def remove(self,index): 

        if self.head is None:
            print("linked list is empty")

        if index==0:
                head=head.link

        else:
            itr = self.head # latest node
            count = 0
            while itr:
                if count == index - 1:
                    itr.link = itr.link.link
                itr = itr.link
                count += 1

    def insert(self,index,data): # 2
        # newnode=node(data,)
        itr=self.head
        count=0
        if index==0:
            self.append(data)
        while itr:
                if count == index-1 : # 1.link
                    itr.link = node(data,itr.link)
                    self.ctr += 1
                    break
                itr = itr.link
                count += 1

    # def insert(self,index,data):
    #     new_node=node(data,self.head)
    #     if self.head is None:
    #         self.head=new_node
    #     else:
    #         itr=self.head
    #         while index!=0:
    #             itr=itr.link
    #             index-=1
    #         if itr is self.head:
    #             new_node.link=self.head
    #             self.head=new_node
    #         else:
    #             new_node.link=itr.link
    #             itr.link=new_node




obj = linkedlist()

print("Is_empty : ", obj.is_empty())

obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.display()

print()
# print("Is_empty : ", obj.is_empty())

# print("Length : ",obj.length())

# obj.remove(1)

obj.insert(2,100)

obj.display()