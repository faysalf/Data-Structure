class Node:
    def __init__(self,data):
        self.value = data      #self.value variable data rakhi
        self.next = None       #next None

class LinkedList:
    def __init__(self):
        self.head = None        #head none kore nilam

    def Push(self,new_data):
        new_node = Node(new_data)   #Node akare data rakhlam
        new_node.next = self.head   #swap kore dilam
        self.head = new_node

    def InsertAfter(self,previous_node,new_data): #previous datar pore new_data bosbe
        if previous_node is None:
            print("Previous node must be in")
            return

        new_node = Node(new_data)
        new_node.next = previous_node.next  #now previous_node.next == empty
        previous_node.next = new_node       #swaping

    def Append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    #delete or remove
    def delete_with_position(self,position):
        if self.head is None:
            return
        else:
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            temp.next = temp.next.next

    def delete_data(self,data):
        if self.head is None:
            return
        elif self.head.value == data:
            self.head = self.head.next

        temp = self.head
        while temp.next is not None:
            if temp.next.value == data:
                break
            else:
                temp = temp.next
        temp.next = temp.next.next
        return

#Linked List Traversal
    def ListTraverse(self):
        temp = self.head.next.next
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next

#Linked List Reverse
    def reverse(self):          #Details in data structure E.B
        previous = None
        current_node = self.head
        while current_node is not None:
            next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next
        self.head = previous


    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

if __name__=="__main__":
    info = LinkedList()
    info.Push("Last Push")
    info.Push(20)
    info.Push(30)
    info.Push(10)
    info.Print()
    print()
    info.InsertAfter(info.head.next, "InsertAfter")
    info.Append("Append")
    info.Print()
    print()
    info.delete_with_position(2)
    info.Print()
    info.delete_data(30)
    print()
    info.Print()
    print()
    info.Append("After Delete")
    info.Append(60)
    info.Append(70)
    info.Print()
    print()
    info.ListTraverse()
    print()
    print("After reverse")
    info.reverse()
    info.Print()

