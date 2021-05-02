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

    def swaping(self,data1,data2):
        if data1==data2:
            return

        temp = self.head
        while temp is not None: #er against a while temp: likhleo hoy
            if temp.value == data1:
                temp.value = data2
            elif temp.value == data2:
                temp.value = data1
            temp = temp.next

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
    print("\nBefore swaping:")
    info.Print()
    info.swaping(3,5)
    print("\n\nAfter swaping:")
    info.Print()