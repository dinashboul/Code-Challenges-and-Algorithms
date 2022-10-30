# Write here the code challenge solution

from os import link
from platform import node


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

    def __str__(self):
        '''its to print all the nodes in the list'''
        nodes=""
        if self.head is None:
            nodes="empty"
        else:
            temp=self.head
            while temp:
                nodes+=f"{temp.value}>"
                temp=temp.next
            nodes+="None"
        return nodes


    def printAll(self):

        ''' printAll method to print the nodes from middle to none'''
        nodes=[]
        if self.head is None:
            return(" empty")
        else:
            current = self.Print_Middle()
            while current is not None:
                nodes.append(current.value)
                current = current.next
            return nodes
        
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
        slow = self.head
        fast = self.head
        while fast:
             fast=fast.next
             if fast:
                fast=fast.next
             else:
                break
             slow = slow.next 
        return slow

    


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

    # print(linkedList1)
    print(linkedList1.printAll())
