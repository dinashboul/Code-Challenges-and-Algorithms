# Write here the code challenge solution
from multiprocessing.sharedctypes import Value
from os import cpu_count
from platform import node


class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

'''
Linked List class :Its class to create  a linked list
'''
class Linked_list():
    def __init__(self):
        self.head=None
    
    '''
    method append to add new node to the linked list
    '''
    def append_node(self,node):
        if self.head==None:
            self.head=node
        
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=node

    '''
    method print_all is to print all the nodes in linked list
    '''
    def print_all(self):
        nodes=[]
        if self.head==None:
            return
        else:
            current=self.head
            while current is not None:
                # print(current.value)
                nodes.append(current.value)
                current=current.next
            return nodes
    
     
    '''
       Remove_nth_node method: remove the nth node from the end of the list and return its head.
     '''
    def Remove_nth_node(self, n):
        fast = self.head
        slow = self.head
                                                                                
        for i in range(n):
            fast = fast.next
    
        if not fast:
            return self.head.next

        

        while fast.next:
            fast = fast.next
            slow = slow.next
 
        slow.next = slow.next.next
        return self.head


            

if __name__=="__main__":
    ll1=Linked_list()    
    node1=Node("1")
    ll1.append_node(node1)

    node1=Node("2")
    ll1.append_node(node1)

    node1=Node("3")
    ll1.append_node(node1)

    node1=Node("4")
    ll1.append_node(node1)

    ll1.Remove_nth_node(3)
    print("the nth value is------>",ll1.print_all()
)
    
    
    
