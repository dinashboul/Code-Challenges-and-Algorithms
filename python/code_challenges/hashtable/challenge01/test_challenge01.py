# Write your test here
import pytest
from challenge01 import *
def test_find_sum():
    tree=Tree()
    tree.root = Node(7)
    tree.root.left = Node(4)
    tree.root.right = Node(8)           
    tree.root.right.right = Node(10)
    tree.root.left.right = Node(5)
    tree.root.left.left = Node(2)    
    assert  findTarget(tree.root, 20)==False

def test_find_sum_TRUE():
    tree=Tree()
    tree.root = Node(7)
    tree.root.left = Node(4)
    tree.root.right = Node(8)
    tree.root.right.right = Node(10)
    tree.root.left.right = Node(5)
    tree.root.left.left = Node(2)    
    assert  findTarget(tree.root, 13)==True