# Write your test here
import pytest 

from challenge03 import Linked_list,Node

def test_remove_nth():
    ll1=Linked_list()    
    node1=Node("A")
    ll1.append_node(node1)

    node1=Node("B")
    ll1.append_node(node1)

    node1=Node("C")
    ll1.append_node(node1)

    node1=Node("D")
    ll1.append_node(node1)
    ll1.Remove_nth_node(3)
    actual =   ll1.print_all()
    expected = ['A', 'C', 'D']
    assert actual == expected

def test_if_n_greater_than_count():
    ll1=Linked_list()    
    node1=Node("A")
    ll1.append_node(node1)

    node1=Node("B")
    ll1.append_node(node1)

    node1=Node("C")
    ll1.append_node(node1)

    node1=Node("D")
    ll1.append_node(node1)
    ll1.Remove_nth_node(5)
    actual =   ll1.print_all()
    expected = ['A', 'B', 'C', 'D'] 
    assert actual == expected

def test_if_linkedList_is_empty():
    ll1=Linked_list()    
    ll1.Remove_nth_node(5)
    actual =   ll1.print_all()
    expected = None
    assert actual == expected


