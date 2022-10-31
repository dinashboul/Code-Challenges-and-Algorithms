# Write your test here
import pytest
from challenge02 import brackets

def test_wrong_seq():
    seq="{[(])}"
    actual=brackets(seq)
    expected= False
    assert actual== expected

def test_correct_seq():
    seq="{[()]}"
    actual=brackets(seq)
    expected= True
    assert actual== expected


def test_seq_with_word():
    seq="[(hello)()]"
    actual=brackets(seq)
    expected= True
    assert actual== expected
