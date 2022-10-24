# Write here the code challenge solution

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
'''
Linked List class :Its class to create  a linked list
'''
class LinkedList:
    def __init__(self):
        self.head = None
    '''
    method append to add new node to the linked list
    '''
    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
   
    ''' 
    Function Print_middle its method to print the middle of the linked list 
    >>> If there are two middle nodes, will return the second middle node.
    '''

    def Print_Middle(self):
        nodes=[]
        curr = self.head
        my_len = 0
        while curr:
            curr = curr.next
            my_len = my_len + 1

        curr =self.head
        for i in range((my_len )//2):
            curr = curr.next

        while curr!=None:
            if my_len % 2 == 0:
                 nodes.append(curr.value)
                 curr=curr.next
            else:
                nodes.append(curr.value)
                curr=curr.next  
      
        return nodes



if __name__ == "__main__":
    linkedList1 = LinkedList()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)

    node5 = Node("E")
    linkedList1.append(node5)

    node6 = Node("F")
    linkedList1.append(node6)

    node7= Node("G")
    linkedList1.append(node7)

    
    # print("the middle node is ",linkedList1.Print_Middle())
    print("the middle is",linkedList1.Print_Middle())