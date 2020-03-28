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
    def get_verices(self):
        for a in self.parse_all():
            print(a)

    # function to add an edge using the 2 points: a and b if there is no edge like that yet
    def add_edge(self, a, b, c):
        if a in self._dict.keys() and (b not in self.parse_out_n(a)):
            self._dict[a].append(b)
        #the cost of the edge
            self._cost["%s - %s" %(a,b)] = []
            self._cost["%s - %s" %(a,b)].append(c)
            print(self._cost)
        else:
            print(fg(124) + "Edge already exists !" + fg.rs)

    # function that removes an edge from point a to b if it
    def delete_edge(self, a, b):
        if a in self.parse_all():
            if b in self.parse_out_n(a):
                

    # function that adds a vertex a
    def add_vertex(self, a):
        if a not in self._dict.keys():
            self._dict[a] = []
        else:
            print(fg(124) + "Vertex already exists !" + fg.rs)

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
            for y in self.parse_out_n(x):
                c = self._cost["%s - %s" % (x, y)]
                print(fg(220) + ("%s -> %s  cost: %s" % (x, y, c)) + fg.rs)


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
        if command == "adde":
            point_a = int(input("Enter point a: "))
            point_b = int(input("Enter point b: "))
            cost = int(input("Enter the cost of the edge: "))
            g.add_edge(point_a, point_b, cost)
        elif command == "addv":
            vertex = int(input("Enter a number for the vertex: "))
            g.add_vertex(vertex)
        elif command == "dele":
            point_a = int(input("Enter point a: "))
            point_b = int(input("Enter point b: "))

        elif command == "1":
            g.list_graph()
        elif command == "2":
            print_menu()
        elif command == "3":
            print(g.count_vertices())
        elif command == "4":
            g.get_verices()
        elif command == "5":
            point_a = int(input("Enter point a: "))
            point_b = int(input("Enter point b: "))
            if g.verify_edge(point_a, point_b):
                print("There exists an edge from %s to %s !" % (point_a, point_b))
            else:
                print("No such edge exists !")
        #elif command == "6":
        #elif command == "7":
        #elif command == "8":
        #elif command == "9":
        #elif command == "10":
        else:
            print(fg(124) + "Not a valid command !" + fg.rs)

run()
