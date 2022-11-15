
# Write your test here
import pytest
from challenge01 import *
def test_Bt_traversal():
    tree=Tree()
    tree.root = Node(6)
    tree.root.left = Node(7)
    tree.root.right = Node(8)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(10)
    bt=BT_traversal(Preorder_traversal(tree.root),Inorder_traversal(tree.root))
    actual=breadth_taversal(bt)
    expected=[6, 7, 8, 9, 10]
    assert actual == expected

