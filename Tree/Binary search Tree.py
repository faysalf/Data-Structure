class TreeNode:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return repr(self.value)

    def add_left(self,node):
        self.left = node
        if node is not None:       #node khali na hole er root takee parent a rekhe dibo
            self.parent = self

    def add_right(self,node):
        self.left = node
        if node is not None:
            self.parent = self
#data insert
def BST_Insert(root,node):
    last_node = None
    curent_node = root

    while curent_node is not None:
        last_node = curent_node             #last_node a shesh node asbe current_node hoye.
        if curent_node.value > node.value:  #node chhuto hole left site a position dekhbe
            curent_node = curent_node.left
        else:
            curent_node = curent_node.right #nahoy right site position khujbe

    if last_node is None:                   #last_node None howa mane tree khali. tokhon amra root a node call korbo
        root = node
    elif last_node.value > node.value:        #node chhuto hole root er left a node bosabe. root.left.right o hote pare.
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root

#Traversing
def BST_Create():
    root = TreeNode(10)
    l = [17,5,3,7,12,19,1,4]
    for item in l:
        node = TreeNode(item)
        root = BST_Insert(root,node)

    return root

if __name__=="__main__":
    info = BST_Create()
    print(info)