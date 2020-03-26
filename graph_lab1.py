# Mos Daniele
# Gp: 915

# Languages for implementation: Python 

class Graph:
    """To represent a directed graph, we will use 3 disctionaries: 
        1) for vertex to outbound neighbours
        2) for vertex to inbound neighbours
        3) edges and their cost """

    # create a graph: n vertices (0 to n-1) and without edges
    def __init__(self, n):
        self._dict = {}
        for i in range(n):
            self._dict[i] = []
        
    # returns all the edges with their associated cost
    def get_edges(self):

    # function to add an edge using the 2 points: a and b if there is no edge like that yet
    def add_edge(self, a, b, c):

    # function that removes an edge from point a to b if it
    def delete_edge(self, x, y):

    # function that adds a vertex a
    def add_vertex(self, a):

    # returns the number of vertices    
    def count_vertices(self):
       
    # returns the number of edges   
    def count_edges(self):

    # returns an iterable with all vertices
    def parse_all(self):

    # returns an iterable with outbound neighbours of the parameter a
    def parse_out_n(self, a):

    # returns an iterable with inbound neighbours of the parameter a
    def parse_in_n(self, a):

    # returns "True" if there exists an edge from the 2 given points (a and b), "False" otherwise
    def verify_edge(self, a, b):

    # returns "True" if a is a vertex, "False" otherwise
    def verify_vertex(self, a):

    # returns the in degree of the vertex v
    def degree_in(self, v):

    # returns the out degree of the vertex v
    def degree_out(self, v):

    # function that deletes a vertex if it exists
    def delete_vertex(self, a):

    # returns the cost of the edge from a to b, if it exists
    def edge_cost(self, a, b):

    # function that allows the user to change the cost of an edge from a to b
    def set_edge_cost(self, a, b, c):

    # returns iterator for verices
    def iterator_vertices(self):

    # returns iterator for out edges of vertex v
    def iterator_outedg(self,v):

    # returns iterator for in edges of vertex v
    def iteartor_inedg(self,v):

    # prints the graph like so: a -> b (the cost of the edge)
    def list_graph(self, x):


    # returns an iterable structure for given x
class Iterator:
    def __init__(self,x):