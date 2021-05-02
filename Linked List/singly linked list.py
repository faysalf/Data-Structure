class Node:
    def __init__(self,data):
        self.val = data         #self.val variable a data rakhlam
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None        #self.head ke very first a khali kore rakhlam

    def New_Data_Append(self,new_data):
        current_data = Node(new_data)   #Node er rules a current_data y rakhlam new_data ke
        if self.head is None:           #head jodi khali thake
            self.head = current_data    #tahole head new data ke rekhe dibo
            return

        temp = self.head
        while temp.next is not None: #else head er porer ghorgulu dekhbo khali ase kina
            temp = temp.next
        temp.next = current_data        #khali ghor pawar por sekhane data store korbo
    #print (Traversing avabee kore)
    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next

if __name__=="__main__":
    #data append
    info = linkedlist()
    info.New_Data_Append(90)
    info.New_Data_Append(40)
    info.New_Data_Append("Faysal")
    info.New_Data_Append("GPA: 4.44")
    #data print
    info.print_linkedlist()