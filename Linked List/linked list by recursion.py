class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

def Append(head,data):
    if head == None:        #head None hole return None
        return Node(data)   #Class chara addressing kora jayna. tai Noder
                            #vitore niye return korechhi.alada def ao call kore nite pari

#head.next call kora hoyechhe.condition True hole head.next akbar beshi
#cholbe. tai akbar kom I mean head.next er poriborte head return korbe
    head.next = Append(head.next,data)
    return head

#Push a firs a data input kore
def Push(head,data):
    current_Node = Node(data)

    current_Node.next = head
    head = current_Node
    return head

'''def insertNth(position,data):
    current_node = Node(data)
    current_node.next = position
    position = current_node
    return current_node
'''
def Traverse(head):
    if head == None:
        return
    print(head.value, end=" ")
    Traverse(head.next)

#delet linked list
def delete(head):
    if head == None:
        return
    delete(head.next)           #jeheto value change hocche, but return nei

#delete an element of linked list
def keydelete(head,key):
    if key <= 0:
        print("Enter Positive key")
        return

    if key==1:
        res = head.next
        return res          #key=1 hole head a head.next rakhlee hobe
    head.next = keydelete(head.next,key-1)  #key-1, cause key er maddhomee
                #jacchi.key jotokkhonna 1 hobe totokkhon head.next cholte thakbe
    return head
#Reverse list
def Reverse(node):
    if (node == None) or (node.next == None):
        return node

    new_node = Reverse(node.next)
    node.next.next = node
    node.next = None
    return new_node

if __name__=="__main__":
    head = None                 # head = None. Cause nexter Append head
                                # khuje pabena
    head = Append(head,10)      #1st er head ke base kore 'Append(head,10)'
    head = Append(head,20)
    head = Append(head,30)      #3rd er head ke base kore
    head = Push(head,5)
    Traverse(head)
    print("\nKey no 2 delete")
    head = keydelete(head,2)
    Traverse(head)
    print("\nReverse list")
    head = Reverse(head)
    Traverse(head)
    print('\ndeleting list')
    head = delete(head)
    Traverse(head)
    print("Deleted list")