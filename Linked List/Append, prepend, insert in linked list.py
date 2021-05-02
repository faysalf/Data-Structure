class node:
    def __init__(self,data):
        self.val = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def Append(self,new_data):
        current_data = node(new_data)
        if self.head is None:
            self.head = current_data
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = current_data
    #prepend mane shurute bosbe
    def Prepend(self,new_data):
        current_data = node(new_data)
        current_data.next = self.head
        self.head = current_data

    #insertion
    def insert(self,position,new_data):
        if position is None:
            print("Position must needed")
            return

        current_node = node(new_data)

        current_node.next = position.next
        position.next = current_node

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next

if __name__== "__main__":
    info = linklist()
    info.Append(12)
    info.Append("Hosne Mobarok")
    info.Append(100)
    info.Prepend("prepend: Faysal")
    position = info.head.next
    info.insert(position,"insert: Boss")
    info.insert(info.head.next.next.next.next,"Alhamdulillah")
    info.print()