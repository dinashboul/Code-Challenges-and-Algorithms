# Write your test here
from challenge01 import Stack,Queue
import pytest

queue1=Queue()
queue1.enQueue("A")
queue1.enQueue("B")
queue1.enQueue("C")
queue1.enQueue("D")
queue1.enQueue("E")


def test_dequeue_pop():
    actual = queue1.de_queue()
    expected = "A"
    assert actual == expected

def test_Queue_peek():
    actual=queue1.peek()
    expected= "B"
    assert actual == expected

def test_Queue_empty():
    for i in range(5):
        print(queue1.de_queue())
    actual=queue1.empty()
    expected= False
    assert actual == expected