# Write here the code challenge solution

class Node :
    def __init__(self,value) :
        self.left=None
        self.right=None
        self.value=value

   


def Sorted_to_Bts(num):
    length=len(num)
    if  not length:
        return None
    num.sort()

    mid=length//2
    node=Node(num[mid])
    node.left=Sorted_to_Bts(num[:mid])
    node.right=Sorted_to_Bts(num[mid+1:])
    return node



        
def breadth_taversal(root):
    if root is None:
        return
    queue = []
 
    
    queue.append(root)
    list=[]
    while(len(queue) > 0):
        print(queue[0].value)
        list.append(queue[0].value)
        node = queue.pop(0)
        if node is None:
            print("null")   
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
    return list
        
if __name__=="__main__":
    array = [0,-3,-10,5,9]
    array2=[1,3]
    node=Sorted_to_Bts(array2)
    breadth_taversal(node)
    
    
