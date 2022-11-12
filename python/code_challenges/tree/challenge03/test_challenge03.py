# Write your test here
import pytest
from challenge03 import breadth_taversal,Sorted_to_Bts

def test_sorted_array():
    array = [1,2,3,4,5,6]
    
    node=Sorted_to_Bts(array)
    
    assert breadth_taversal(node)==[4, 2, 6, 1, 3, 5]