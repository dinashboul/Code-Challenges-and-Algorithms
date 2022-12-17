# Write your test here
import pytest
from challenge01 import *
def test_find_sum_false():
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2)  
    s=set() 
    assert  tsB(tree.root, 20,s)==False

def test_find_sum_TRUE():
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2)  
    s=set()     
    assert  tsB(tree.root, 13,s)==True