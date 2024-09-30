""" Description:
Your task is to determine whether every spanning tree of a given graph has the same weight.
Implement a class SameWeight with the following methods:

add_edge adds an edge of weight x between the nodes a and b
check reports whether all spanning trees have the same weight (if the graph is not connected the result should be True)

Implement the class in a file sameweight.py according to the following template:
"""


class SameWeight:
    def __init__(self, n):
        # TODO
        pass

    def add_edge(self, a, b, x):
        # TODO
        pass

    def check(self):
        # TODO
        pass

if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1, 2, 2)
    s.add_edge(1, 3, 3)
    print(s.check()) # True
    s.add_edge(1, 4, 3)
    print(s.check()) # True
    s.add_edge(3, 4, 3)
    print(s.check()) # True
    s.add_edge(2, 4, 1)
    print(s.check()) # False