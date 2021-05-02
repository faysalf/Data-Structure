class Node:
    def __init__(self,data):    #constructor method. class ke initialize korte pythoner reserved kora ai func ke use kore
        self.value = data
        self.left = None
        self.right = None

    '''__repr__ is a special method used to represent a class’s objects as a string.
    __repr__ is called by the repr() built- in function.'''

    def __repr__(self):
        return repr(self.value)
    def add_left(self,left_data):
        self.left = left_data

    def add_right(self,right_data):
        self.right = right_data

def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)

    two.add_left(seven)
    two.add_right(nine)

    one = Node(1)
    six = Node(6)

    seven.add_left(one)
    seven.add_right(six)

    five = Node(5)
    ten = Node(10)

    six.add_left(five)
    six.add_right(ten)

    eight = Node(8)
    nine.add_right(eight)

    three = Node(3)
    four = Node(4)

    eight.add_left(three)
    eight.add_right(four)

    return two

#Traversing Tree
def PreOrder(node):     #Root -- Left -- Right
    print(node,end= " ")
    if node.left:   #if node.left is not None
        PreOrder(node.left)
    if node.right:
        PreOrder(node.right)

def PostOrder(node):    #left -- right -- Root
    if node.left:
        PostOrder(node.left)
    if node.right:
        PostOrder(node.right)
    print(node,end=" ")

def InOrder(node):
    if node.left:
        InOrder(node.left)
    print(node,end=" ")
    if node.right:
        InOrder(node.right)

if __name__=="__main__":
    info = create_tree()
    print("PreOrder: ")
    PreOrder(info)
    print("\n\nPostOrder: ")
    PostOrder(info)
    print("\n\nInOrder: ")
    InOrder(info)