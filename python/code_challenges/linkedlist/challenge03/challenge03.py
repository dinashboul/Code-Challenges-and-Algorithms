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
        self.next=None
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
        countList = self.head
        count = 1
        
        if self.head==None:
            return
        while countList.next is not None:
            count+=1
            countList = countList.next
        if n> count :
            print(f"please enter number less than or equal {count}")
            return
        countList = self.head
        temp = self.head
        i = 0

        while i<=count:
            if(i!= count-n):
                temp = countList
                countList = countList.next
                i+=1
            else:
                if temp.next != None and countList!=self.head:
                    temp.next = countList.next
                    countList.next=None
                    break
                else:
                    self.head = self.head.next
                    countList.next=None
                    return self.head
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
    node1=Node("5")
    ll1.append_node(node1)

    ll1.Remove_nth_node(3)
   
    
    print("the nth value is------>",ll1.print_all())
    
    
    
