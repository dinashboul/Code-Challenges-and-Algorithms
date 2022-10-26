# Write your test here
import pytest 

from challenge03 import Linked_list,Node

def test_remove_nth():
    ll1=Linked_list()    
    node1=Node("1")
    ll1.append_node(node1)

    node1=Node("2")
    ll1.append_node(node1)

    node1=Node("3")
    ll1.append_node(node1)

    node1=Node("4")
    ll1.append_node(node1)
    ll1.Remove_nth_node(ll1.head, 3)
    actual =   ll1.print_all()
    expected = ['1', '2', '4']
    assert actual == expected

