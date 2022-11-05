# Write your test here
import pytest
from challenge01 import Node,Ordering

def test_Bt_traversal():
    order=Ordering()
    preorder=[3,9,20,15,7]
    inorder=[9,3,15,20,7]
    actual=order.BT_traversal(preorder,inorder).value
    expected=3
    assert actual == expected

def test_one_element():
    order1=Ordering()
    preorder=[3]
    inorder=[3]
    actual=order1.BT_traversal(preorder,inorder)
    expected=3
    assert actual == expected