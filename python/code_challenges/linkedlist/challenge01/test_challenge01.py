# Write your test here
from re import A
import pytest 
from challenge01 import LinkedList,Node,Delete_node

linkedList1 = LinkedList()
node1 = Node("1")
linkedList1.append(node1)

node2 = Node("2")
linkedList1.append(node2)

node3 = Node("3")
linkedList1.append(node3)

node4 = Node("4")
linkedList1.append(node4)




def test_append_node():
    assert linkedList1.printAll()==['1', '2','3','4']




def test_delete_node ():
  delete_node1=Delete_node()
  delete_node1.delete_node(node3)

  assert  linkedList1.printAll() == ['1','2','4']
