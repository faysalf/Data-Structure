class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def Data_append(self,new_data):
        current_data = Node(new_data)
        if self.head is None:
            self.head = current_data
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = current_data

    def printlinkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next

if __name__=="__main__":
    res = linkedlist()
    res.Data_append(10)
    res.Data_append(300)
    res.Data_append(20)
    res.Data_append(5)
    res.printlinkedlist()