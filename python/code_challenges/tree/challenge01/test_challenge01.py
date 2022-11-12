# Write your test here
import pytest
from challenge01 import Node,Ordering

def test_Bt_traversal():
    tree=Ordering()

    assert tree.BT_traversal([3,9,20,15,7],[9,3,15,20,7]).value == [3]
    assert tree.BT_traversal([3,9,20,15,7],[9,3,15,20,7]).left.value == 9
    assert tree.BT_traversal([3,9,20,15,7],[9,3,15,20,7]).right.value == 20
    assert tree.BT_traversal([3,9,20,15,7],[9,3,15,20,7]).right.left.value == 15
    assert tree.BT_traversal([3,9,20,15,7],[9,3,15,20,7]).right.right.value == 7


def test_one_element():
    order1=Ordering()
    preorder=[3]
    inorder=[3]
    actual=order1.BT_traversal(preorder,inorder)
    expected=3
    assert actual == expected