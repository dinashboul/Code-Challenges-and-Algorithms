# Write here the code challenge solution

class Node :
    def __init__(self,value) :
        self. value=value
        self.right=None
        self.left=None

class Tree:
    def __init__(self):
        self.root = None


list_in=[]

def Inorder_traversal(root):
    if root.left is not None:
       Inorder_traversal(root.left)
    if root is not None:
        list_in.append(root.value)
    if root.right is not None:
        Inorder_traversal(root.right)
    return list_in

list_pre=[]
def Preorder_traversal(root):
    if root is not None:
        list_pre.append(root.value)
    if root.left is not None:
       Preorder_traversal(root.left)
    if root.right is not None:
        Preorder_traversal(root.right)
    return list_pre
    
def BT_traversal(preorder,inorder):
    
    if not preorder or not inorder:
            return None
    if len(preorder)==1 and len(inorder)==1:
        root=Node(preorder[0]) 
        return root

    mid = preorder.pop(0)
    root = Node(mid)
    node = inorder.index(mid)
    root.left = BT_traversal(preorder, inorder[:node])
    root.right = BT_traversal(preorder, inorder[node+1:])  
    return root

def breadth_taversal(root):
    new_list = []
    if not root:
        new_list.append(None)
        return
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node.left  :
            q.append(node.left)
        
        if node.right :
            q.append(node.right)
        new_list.append(node.value)
    
    return new_list

if __name__=="__main__":
    
    tree=Tree()
    tree.root = Node(3)
    tree.root.left = Node(2)
    tree.root.right = Node(4)
    tree.root.right.left = Node(1)
    tree.root.right.right = Node(5)
    bt=BT_traversal(Preorder_traversal(tree.root),Inorder_traversal(tree.root))
    print(breadth_taversal(bt))
