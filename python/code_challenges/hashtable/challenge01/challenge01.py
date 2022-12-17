# Write here the code challenge solution
class Tree():
    def __init__(self):
       self.root=None 

class Node :
    def __init__(self,data):
     self.data = data
     self.left = None
     self.right = None



'''
function that takes a Binary Search tree and an integer as a parameter. 
Return True if Binary search tree has two elements that their summation is the given integer.    '''
    
def tsB(root,k,s):
   
    if root:
        if k - root.data in s:
            return True
        s.add(root.data)
        return tsB(root.left,k,s) or tsB(root.right,k,s)
    else:
        return False
        



if __name__ =='__main__':
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2) 
    
    print('\n# #################### two_sum_bst function #################### #\n')
    s = set()

    print(' k=4 => ',tsB(tree.root, 4,s))
    print('k=9 => ',tsB(tree.root, 9,s))
    print('k=5 => ',tsB(tree.root, 5,s))
    print('k=8 => ',tsB(tree.root, 8,s))
    print('k=13 => ',tsB(tree.root, 13,s))
    print('k=20 => ',tsB(tree.root, 20,s))


