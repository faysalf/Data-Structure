class Node:

    def __init__(self, data):
        self.val = data
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)



a.next = b
print(a.next.val)

