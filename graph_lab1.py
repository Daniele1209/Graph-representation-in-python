# Mos Daniele
# Gp: 915

# Languages for implementation: Python

import random
from sty import fg

class Graph:
    """To represent a directed graph, we will use 3 disctionaries: 
        1) for vertex to outbound neighbours
        2) for vertex to inbound neighbours
        3) edges and their cost """

    # create a graph: n vertices (0 to n-1) and without edges, and a list for the cost of each edge
    def __init__(self, n):

        self._cost = {}

        self._dict = {}
        for i in range(n):
            self._dict[i] = []
        
    # returns all the edges with their associated cost
    def get_edges(self):
        for a in self.parse_all():
            print(a)

    # function to add an edge using the 2 points: a and b if there is no edge like that yet
    def add_edge(self, a, b, c):
        self._dict[a].append(b)
        #the cost of the edge
        self._cost["%s - %s" %(b,a)] = []
        self._cost["%s - %s" %(b,a)].append(c)
        #print(self._cost)

    # function that removes an edge from point a to b if it
  #  def delete_edge(self, x, y):

    # function that adds a vertex a
  #  def add_vertex(self, a):


    # returns the number of vertices    
    def count_vertices(self):
        count = 0
        for i in self._cost.keys():
            count += 1
        return count
    # returns the number of edges   
  #  def count_edges(self):

    # returns an iterable with all vertices
    def parse_all(self):
        return self._dict.keys()

    # returns an iterable with outbound neighbours of the parameter a
    def parse_out_n(self, a):
        return self._dict[a]

    # returns an iterable with inbound neighbours of the parameter a
    def parse_in_n(self, a):
        list = []
        for elem in self._dict.keys():
            if a in self._dict[elem]:
                list.append(elem)
        return list

    # returns "True" if there exists an edge from the 2 given points (a and b), "False" otherwise
    def verify_edge(self, a, b):
        return b in self._dict[a]

    # returns "True" if a is a vertex, "False" otherwise
 #   def verify_vertex(self, a):

    # returns the in degree of the vertex v
  #  def degree_in(self, v):

    # returns the out degree of the vertex v
 #   def degree_out(self, v):

    # function that deletes a vertex if it exists
  #  def delete_vertex(self, a):

    # returns the cost of the edge from a to b, if it exists
  #  def edge_cost(self, a, b):

    # function that allows the user to change the cost of an edge from a to b
  #  def set_edge_cost(self, a, b, c):

    # returns iterator for verices
  #  def iterator_vertices(self):


    # returns iterator for out edges of vertex v
  #  def iterator_outedg(self,v):

    # returns iterator for in edges of vertex v
  #  def iteartor_inedg(self,v):

    # prints the graph like so: a -> b (the cost of the edge)
    def list_graph(self):
        for x in self.parse_all():
            for y in self.parse_in_n(x):
                c = self._cost["%s - %s" % (x, y)]
                print(fg(220) + ("%s -> %s  cost: %s" % (y, x, c)) + fg.rs)


    # returns an iterable structure for given x
#class Iterator:
 #   def __init__(self,x):

def initMyGraph(ctor):
    """Constructs and returns a hard-coded sample graph.
    ctor must be a callable that gets the number of vertices and
	creates a graph with the given number of vertces and with no edges"""
    f = open("graph_ex.txt", "r")
    stats = f.readline()
    stat = stats.split(" ")
    vertex_nr = int(stat[0])
    g = ctor(vertex_nr)
    for i in f:
        st = i.split(" ")
        point_a = int(st[0])
        point_b = int(st[1])
        cost = int(st[2])
        g.add_edge(point_a, point_b, cost)
    f.close()
    return g

def print_ascii_art():
    f = open("art.txt", "r")
    content = f.read()
    print(fg(209) + content + fg.rs)
    f.close()

def print_menu():
   f = open("commands.txt", "r")
   content = f.read()
   print(fg(45) + content + fg.rs)
   print()
   f.close()

def run():
    print_ascii_art()
    print_menu()
    g = initMyGraph(Graph)
    command = -1
    while(command != "0"):
        command = input(">>> ")
      #  if command == "addv":


        if command == "1":
            g.list_graph()
        if command == "2":
            print_menu()
        if command == "3":
            print(g.count_vertices())
        #if command == "4":
        if command == "5":
            g.get_edges()
        #if command == "6":
        #if command == "7":
        #if command == "8":
        #if command == "9":
        # if command == "10":
        # if command == "11":

run()
