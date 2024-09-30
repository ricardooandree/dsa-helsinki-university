""" Description:
Your task is to implement a class that supports adding an edge to a graph and counting how many different spanning trees the graph has.

Implement a class AllTrees with the following methods:

add_edge adds an edge to the graph
count returns the number of spanning trees
The graph is undirected, and you may assume that there is at most one edge between each pair of nodes.

In this task, a brute force solution is acceptable. You must use a method that you understand yourself (no solution based on matrices unless you can prove the correctness).

Implement the class in a file spanning.py according to the following template:
"""


class AllTrees:
    def __init__(self, n):
        # TODO
        pass

    def add_edge(self, a, b):
        # TODO
        pass

    def count(self):
        # TODO
        pass

if __name__ == "__main__":
    a = AllTrees(3)
    a.add_edge(1, 2)
    print(a.count()) # 0
    a.add_edge(1, 3)
    print(a.count()) # 1
    a.add_edge(2, 3)
    print(a.count()) # 3