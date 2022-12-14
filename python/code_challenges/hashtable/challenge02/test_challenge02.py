# Write your test here
import pytest 
from challenge02 import*
def test_repition():
    input = 'ASAC is a department at LTUC. ASAC teaches '
    assert firstRepeat(input)== 'ASAC'

def test_many_repitition():
    input = 'ASAC is a department at LTUC. ASAC teaches programming in LTUC.'
    assert firstRepeat(input)== 'ASAC'

def test_no_repitition():
    input = 'ASAC is a department at LTUC. '
    assert firstRepeat(input)== None
