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

'''after while loop: jehetu current.next empty kore sekhane head rakhte hobe.
tai next variable a current.next value rakhlam. tarpor empty korlam. jeheto current=next rakhbo,
tai previous a current niye nilam tarpor loop sheseh self.head = previous rekhe diboA'''

    def Reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

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
    info.Reverse()
    info.Print()