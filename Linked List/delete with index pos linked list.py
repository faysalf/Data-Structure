class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def Push(self,new_data):
        current_data = Node(new_data)
        current_data.next = self.head
        self.head = current_data

    def delete_in_index(self,position):
        if position==0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
            temp.next = temp.next.next

    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next

if __name__=="__main__":
    info = linkedlist()
    l = [1,2,3,4,5,6]   #agulu push korbo
    for i in l:
        info.Push(i)
    print("\nBefore deleting: ")
    info.Print()
    info.delete_in_index(3)
    print("\n\nAfter deleting:")
    info.Print()