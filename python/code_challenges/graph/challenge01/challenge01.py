
#////////////////////////// Class Node /////////////////////////////////////

class Node :
    def __init__(self,value =None):
        self.value=value

    def __str__(self) :
        return self.value

class Edge:
    def __init__(self,vertex,weight=0) :
        self.vertex=vertex
        self.weight=weight
#////////////////////////// Class Graph/////////////////////////////////////

class Graph:
    def __init__(self) :
        self.adj_list={}

    def add_node (self,value):
        new_vertex=Node(value)
        self.adj_list[new_vertex]=[]
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return ("this node doesnot exist")

        edge1=Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2=Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output


    
    def bfs(self, startVertex):
        '''
        A methode that takes value and traverse through the graph and return a list of nodes
        '''
        visited = set()
        queue = []
        graph_nodes = []

        visited.add(startVertex)
        queue.append(startVertex)


        while queue:
            gnodes = queue.pop(0)
            graph_nodes.append(gnodes.value)
            for i in self.adj_list[gnodes]:
                if i.vertex not in visited:
                    queue.append(i.vertex)
                    visited.add(i.vertex)
        return graph_nodes

if __name__ == "__main__":
    graph1=Graph()
    a=graph1.add_node("A")
    b=graph1.add_node("B")
    c=graph1.add_node("C")
    d=graph1.add_node("D")
    e=graph1.add_node("E")
    f=graph1.add_node("F")

    
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(a,e)
    graph1.add_edge(b,d)
    graph1.add_edge(d,e)
    
    graph1.add_edge(e,f)
    
    graph1.add_edge(c,f)

    # print(graph1)

    print(graph1.bfs(a))