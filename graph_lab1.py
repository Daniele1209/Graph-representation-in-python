# Mos Daniele
# Gp: 915

# Languages for implementation: Python

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from sty import fg

class Graph:

    # create a graph: n vertices (0 to n-1) and without edges, and a list for the cost of each edge
    def __init__(self, n):
        self._cost = {}

        self._dict = {}
        for i in range(n):
            self._dict[i] = []
        
    # returns all the edges with their associated cost
    def get_vertices(self):
        for a in self.parse_all():
            print(a)

    # function to add an edge using the 2 points: a and b if there is no edge like that yet
    def add_edge(self, a, b, c):
        if a in self.parse_all() and (b not in self.parse_out_n(a)):
            self._dict[a].append(b)
        #the cost of the edge
            self._cost["%s - %s" %(a,b)] = c
        else:
            print(fg(124) + "Edge not valid !" + fg.rs)

    # function that removes an edge from point a to b if it and its associated cost
    def delete_edge(self, a, b):
        if a in self.parse_all():
            if b in self.parse_out_n(a):
                elem = self._dict[a]
                del self._cost["%s - %s" %(a,b)]
                elem.remove(b)
            else:
                print(fg(124) + "Point b does not exist !" + fg.rs)
        else:
            print(fg(124) + "Point a does not exist !" + fg.rs)


    # function that adds a vertex a
    def add_vertex(self, a):
        if a not in self.parse_all():
            self._dict[a] = []
        else:
            print(fg(124) + "Vertex already exists !" + fg.rs)

    # function that deletes a vertex if it exists
    def delete_vertex(self, a):
        if a in self.parse_all():
            #delete all the edges that come from the chosen vertex
            for b in self.parse_out_n(a):
                del self._cost["%s - %s" %(a, b)]

            del self._dict[a]

            #delete all the edges that come to the chosen vertex
            for e in self.parse_in_n(a):
                elem = self._dict[e]
                del self._cost["%s - %s" %(e,a)]
                elem.remove(a)
        else:
            print(fg(124) + "No such vertex exists !" + fg.rs)

    # returns the number of vertices    
    def count_vertices(self):
        count = 0
        for i in self._dict.keys():
            count += 1
        return count

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

    def parse_cost_all(self):
        return self._cost.keys()

    def parse_cost_n(self, a):
        return self._cost[a]

    # returns "True" if there exists an edge from the 2 given points (a and b), "False" otherwise
    def verify_edge(self, a, b):
        return b in self._dict[a]

    # returns "True" if a is a vertex, "False" otherwise
    def verify_vertex(self, a):
        return a in self._dict.keys()

    # returns the in degree of the vertex v
    def degree_in(self, v):
        if self.verify_vertex(v):
            return(self.parse_in_n(v))
        else:
            print(fg(124) + "No such vertex exists !" + fg.rs)

    # returns the out degree of the vertex v
    def degree_out(self, v):
        if self.verify_vertex(v):
            return(self.parse_out_n(v))
        else:
            print(fg(124) + "No such vertex exists !" + fg.rs)

    # returns the cost of the edge from a to b, if it exists
    def edge_cost(self, a, b):
        return self._cost["%s - %s" %(a,b)]

    # function that allows the user to change the cost of an edge from a to b
    def set_edge_cost(self, a, b, c):
        self._cost["%s - %s" %(a,b)] = c

    # prints the graph like so: a -> b (the cost of the edge)
    def list_graph(self):
        for x in self.parse_all():
            for y in self.parse_out_n(x):
                c = self._cost["%s - %s" % (x, y)]
                print(fg(220) + ("%s -> %s  cost: %s" % (x, y, c)) + fg.rs)

    def graph_repres(self):
        list_var = {}
        from_var = []
        to_var = []

        for i in self._dict.keys():
            for j in self._dict[i]:
                from_var.append(i)
                to_var.append(j)

        list_var['from'] = from_var
        list_var['to'] = to_var
        df = pd.DataFrame(list_var)
        G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())
        nx.draw(G, with_labels=True, node_size=400, alpha=0.3, arrows=True)
        plt.show()

def print_fct(visited_list, root, number_indents):
    if visited_list == {}:
        return 0
    print(("\t" * number_indents) + str(root) + "\n")
    number_indents = number_indents + 1
    while len(visited_list[root]):
        print_fct(visited_list, (visited_list[root])[0], number_indents)
        (visited_list[root]).pop(0)

def reconstruct_path(start, end, prev, graph):
    path = []
    elem = end
    while elem:
        path.append(elem)
        try: elem = prev[elem]
        except KeyError:
            break
    path.reverse()
    if path[0] == start:
        return path
    else:
        return 0

def solve_bfs(start_vert, end_vert, graph):
    prev = bfs(start_vert, graph)
    return reconstruct_path(start_vert, end_vert, prev, graph)


def bfs(vertex, graph):
    visited_list = {}
    queue = []
    queue.append(vertex)
    visited_list[vertex] = []
    prev = {}

    while queue:
        vert = queue.pop(0)
        for v in graph.parse_out_n(vert):
            if v not in visited_list:
                queue.append(v)
                visited_list[v] = []
                prev[v] = vert
                (visited_list[vert]).append(v)

    return prev

#constructs a graph from the specied txt file
def init_txt_graph(ctor):
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

#creates a random graph with n vertices and m edges
def init_random_graph(ctor, n, m):
    g = ctor(n)
    edges = 0
    if m > n**2:
        return 0
    while edges < m:
        point_a = random.randrange(0, n)
        point_b = random.randrange(0, n)
        if not g.verify_edge(point_a, point_b):
            cost = random.randint(-m * 10, m * 10)
            g.add_edge(point_a, point_b, cost)
            edges += 1
    return g

def copy_current_graph(graph):
    f = open("graph_copy.txt", "w")
    f.write(str(graph.count_vertices()) + "\n")
    for x in graph.parse_all():
        for y in graph.parse_out_n(x):
            c = graph._cost["%s - %s" % (x, y)]
            f.write("%s %s %s\n" % (x, y, c))

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
    ok = True
    print_ascii_art()
    print_menu()
    while(ok):
        print(fg(220) + "Create a graph:   1 - from txt file    2 - random graph" + fg.rs)
        option = input(fg(135) + ">>> " + fg.rs)
        if option == "1":
            g = init_txt_graph(Graph)
            print(fg(46) + "Graph generated successfully" + fg.rs)
            ok = False
        elif option == "2":
            n = int(input("Enter the number of vertices: "))
            m = int(input("Enter the number of edges: "))
            g = init_random_graph(Graph, n, m)
            if g != 0:
                print(fg(46) + "Graph generated successfully" + fg.rs)
                ok = False
            else:
                print("Invalid random graph !")
        else:
            print(fg(124) + "Not a valid option !" + fg.rs)

    command = -1
    while(command != "0"):
        command = input(fg(135) + ">>> " + fg.rs)
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
            g.delete_edge(point_a, point_b)
        elif command == "delv":
            vertex = int(input("Enter vertex: "))
            g.delete_vertex(vertex)
        elif command == "copy":
            copy_current_graph(g)
        elif command == "1":
            g.list_graph()
        elif command == "2":
            print_menu()
        elif command == "3":
            print(g.count_vertices())
        elif command == "4":
            g.get_vertices()
        elif command == "5":
            point_a = int(input("Enter point a: "))
            point_b = int(input("Enter point b: "))
            if g.verify_edge(point_a, point_b):
                print("There exists an edge from %s to %s !" % (point_a, point_b))
            else:
                print("No such edge exists !")
        elif command == "6":
            vertex = int(input("Enter vertex: "))
            print("In degree of vertex %s is: %s" %(vertex, len(g.degree_in(vertex))))
            print("Out degree of vertex %s is: %s" % (vertex, len(g.degree_out(vertex))))
        elif command == "7":
            vertex = int(input("Enter vertex: "))
            print("The list of inbound edges is: " % (g.degree_in(vertex)))
            for elem in g.degree_in(vertex):
                print("%s -> %s" %(elem, vertex))
        elif command == "8":
            vertex = int(input("Enter vertex: "))
            print("The list of outbound edges is: " % (g.degree_out(vertex)))
            for elem in g.degree_out(vertex):
                print("%s -> %s" %(vertex, elem))
        elif command == "9":
            point_a = int(input("Enter point a: "))
            point_b = int(input("Enter point b: "))
            if g.verify_edge(point_a, point_b):
                print("Current cost associated to this edge is: %s" %g.edge_cost(point_a, point_b))
                new_cost = int(input("Enter the new edge cost: "))
                g.set_edge_cost(point_a, point_b, new_cost)
            else:
                print(fg(124) + "No such edge exists !" + fg.rs)
        elif command == "show":
            g.graph_repres()
        elif command == "search":
            vertex_start = int(input("Enter starting vertex: "))
            end_vertex = int(input("Enter ending vertex: "))
            result = solve_bfs(vertex_start,end_vertex, g)
            if result != 0:

                for i in range(len(result)):
                    print(fg(42) + str(result[i]), end = "" + fg.rs)
                    if i < len(result)-1:
                        print(fg(42) + " -> ", end = "" + fg.rs)
                    else:
                        print()
                print(fg(36) + "Length: " + str(len(result)-1) + fg.rs)

            else:
                print("Such path does not exist !")
        else:
            print(fg(124) + "Not a valid command !" + fg.rs)

run()
