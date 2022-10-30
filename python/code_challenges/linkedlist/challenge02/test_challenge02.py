# Write your test here
import pytest
from challenge02 import LinkedList,Node

linkedList1 = LinkedList()
'''
Testing when the number of elements in linked list is odd
'''
def test_Print_Middle_odd():
    node1 = Node("1")
    linkedList1.append(node1)

    node2 = Node("2")
    linkedList1.append(node2)

    node3 = Node("3")
    linkedList1.append(node3)

    node4 = Node("4")
    linkedList1.append(node4)

    node5 = Node("5")
    linkedList1.append(node5)

    node6 = Node("6")
    linkedList1.append(node6)

    node7= Node("7")
    linkedList1.append(node7)
    linkedList1.Print_Middle()
    assert linkedList1.printAll()==['4', '5', '6', '7']


    '''
Testing when the number of elements in linked list is even
'''
def test_Print_Middle_even():
    linkedList2 = LinkedList()
    node1 = Node("1")
    linkedList2.append(node1)

    node2 = Node("2")
    linkedList2.append(node2)

    node3 = Node("3")
    linkedList2.append(node3)

    node4 = Node("4")
    linkedList2.append(node4)

    node5 = Node("5")
    linkedList2.append(node5)

    node6 = Node("6")
    linkedList2.append(node6)

    linkedList2.Print_Middle()
    assert linkedList2.printAll()==['4', '5', '6']

def test_empty_linked_list():
    linkedList3 = LinkedList()
    linkedList3.Print_Middle()
    assert linkedList3.printAll()=='empty'

