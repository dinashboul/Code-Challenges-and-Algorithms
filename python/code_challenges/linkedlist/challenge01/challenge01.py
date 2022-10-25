from ast import Return
from os import preadv


'''
Linked List class :Its class to create  a linked list with 
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
    method print to print all the node in the linked list
    '''
    def printAll(self):
        nodes=[]
        if self.head is None:
            return("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                nodes.append(current.value)
                current = current.next
        
        return nodes


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

'''
methode delete to remove specific node 
'''

def delete_node(node):
    if node == None:
      return 
    else:
      if node.next == None:
        print("Last node can't be remove tail")
        return
      node.value = node.next.value
      node.next = node.next.next
     


        

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

    print(linkedList1.printAll())    
    
    delete_node(node4)
    
    print("list after deleting",linkedList1.printAll())