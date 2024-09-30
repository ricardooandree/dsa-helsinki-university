""" Description:
A graph has n nodes and initially no edges. Your task is to implement a class that can be used for adding an edge to the graph and for checking if the nodes can be colored with two colors so that every edge connects two nodes of different colors.
You may assume that the graph has at most 50 nodes and that the methods of the class are called at most 100 times.
In a file coloring.py, implement a class Coloring with the following methods:

    - constructor with the number of nodes as a parameter
    - add_edge adds an edge between two nodes
    - check checks if the graph can be colored with two colors
"""


class Coloring:
    def __init__(self, n):
        # TODO
        pass

    def add_edge(self, a, b):
        # TODO
        pass

    def check(self):
        # TODO
        pass

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    print(c.check()) # True
    c.add_edge(2, 4)
    print(c.check()) # False