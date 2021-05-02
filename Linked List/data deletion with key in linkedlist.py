#linked list theke element delete
class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None    #self.head emty kore nilam

    def Push(self,new_data):
        current_data = Node(new_data)
        current_data.next = self.head   #head ta ke 1ghor soriye dilam
        self.head = current_data        #tarpor head a current_data rakhlam

    def Delete(self,key):
        if self.head is None:
            return

        if self.head.value == key:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.value == key:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return temp

    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next

if __name__=="__main__":
    info = linkedlist()
    info.Push(9)
    info.Push(8)
    info.Push(7)
    info.Push(6)
    info.Push(56)
    info.Print()
    print()
    #delete
    n = int(input("Enter which you want delete: "))
    info.Delete(n)
    info.Print()