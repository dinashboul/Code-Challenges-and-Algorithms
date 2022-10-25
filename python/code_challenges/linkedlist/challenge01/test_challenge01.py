# Write your test here
from re import A
import pytest 
from challenge01 import LinkedList,Node,delete_node


linkedList1 = LinkedList()
node1 = Node("1")
linkedList1.append(node1)
node2 = Node("2")
linkedList1.append(node2)

node3 = Node("3")
linkedList1.append(node3)

node4 = Node("4")
linkedList1.append(node4)


def test_delete_node():
  delete_node(node2)
  expected = ['1', '3', '4']
  actual = linkedList1.printAll()
  assert actual == expected


def test_delete_tail():
  linkedList2 = LinkedList()
  expected ='The linked list is empty'
  actual = linkedList2.printAll()
  assert actual ==expected
