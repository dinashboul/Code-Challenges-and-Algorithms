# Write here the code challenge solution

 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None



def findTarget( root, k):
    '''
        METHODE to traverce through tree and find two value the summation of these two value equal to given integer
    '''
    nums = []
    inorder(root, nums)
    for i in range(len(nums)):
        if k-nums[i] in nums[i+1:]:
            return True
    return False

def inorder( node, nums):
    if node!=None:
        inorder(node.left, nums)
        nums.append(node.data)
        inorder(node.right, nums)

if __name__ =='__main__':
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2) 
    
    print('\n# #################### two_sum_bst function #################### #\n')

    print(' k=4 => ',findTarget(tree.root, 4))
    print('k=9 => ',findTarget(tree.root, 9))
    print('k=5 => ',findTarget(tree.root, 5))
    print('k=5 => ',findTarget(tree.root, 5))
    print('k=13 => ',findTarget(tree.root, 13))
    print('k=20 => ',findTarget(tree.root, 20))


