# Write your test here
import pytest
from challenge03 import breadth_taversal,Sorted_to_Bts

def test_sorted_array():
    array = [2,3,6,5,1,4]
    
    node=Sorted_to_Bts(array)
    
    assert breadth_taversal(node)==[4, 2, 6 ,  1, 3, 5]


def test_sorted_array_2():
    array = [3,1]

    node=Sorted_to_Bts(array)

    assert breadth_taversal(node)==[3, 1]