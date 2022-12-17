# Write your test here
import pytest
from challenge01 import Node,Graph,Edge

def test_bfs_graph():
    graph2=Graph()
    a=graph2.add_node(1)
    b=graph2.add_node(2)
    c=graph2.add_node(3)
    d=graph2.add_node(4)
    e=graph2.add_node(5)
    f=graph2.add_node(6)
    g=graph2.add_node(7)

    
    graph2.add_edge(a,b)
    graph2.add_edge(a,c)
    graph2.add_edge(c,e)
    graph2.add_edge(b,d)
    graph2.add_edge(b,f)
    
    graph2.add_edge(e,f)
    
    graph2.add_edge(c,g)
    assert graph2.bfs(a)==[1,2,3,4,6,5,7]