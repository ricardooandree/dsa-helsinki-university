""" Description:
You are given a directed acyclic graph, and your task is to count how many different path there are in the graph.

Implement a class AllPaths with the following methods:

    add_edge adds an edge between two nodes
    count returns the number of different paths
    Implement the method count efficiently using dynamic programming.

Implement the class in a file allpaths.py according to the following template:
"""

""" Explanation:
Explanation: The first call to the method count includes the following paths:

1
1 -> 2
1 -> 2 -> 4
1 -> 3
1 -> 3 -> 4
2
2 -> 4
3
3 -> 4
4
"""


class AllPaths:
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
    a = AllPaths(4)
    a.add_edge(1, 2)
    a.add_edge(1, 3)
    a.add_edge(2, 4)
    a.add_edge(3, 4)
    print(a.count()) # 10
    a.add_edge(2, 3)
    print(a.count()) # 14