# Write here the code challenge solution
from collections import deque
import queue

class Node :
    def __init__(self,value) :
        self. value=value
        self.right=None
        self.left=None

class Tree:
    def __init__(self):
        self.root = None

class Ordering:
    
    def BT_traversal(self,preorder,inorder):
      
        if not inorder or not preorder:
            return None
        if len(inorder)==1 or len(preorder)==1:
            return preorder[0]
        
        root =Node(preorder[0])
        mid =inorder.index(preorder[0])
        root.left= self.BT_traversal(preorder[1:mid+1],inorder[:mid])
        root.right = self.BT_traversal(preorder[mid+1:],inorder[mid+1:])
        return root



if __name__=="__main__":
    preorder=[1,2,3,4,5,6,7]
    inorder=[3,2,4,1,6,5,7]
    bt=Ordering()
    print(bt.BT_traversal(preorder,inorder))
    # bt.BT_traversal(preorder,inorder)

