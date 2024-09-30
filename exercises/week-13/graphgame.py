""" Description:
Two players play a game in a directed acyclic graph. There is a single shared token, which is initially in the node x. The players take turns to move the token along a single edge.
The game continues until one of the players has no moves left, because the current node has no edges to other nodes. Then the other player is the winner.
Your task is to design a class GraphGame with the following methods:

    add_link adds an edge from a node a to ta node b
    winning reports if the first player to move wins, when the token is initially in the node x and both players make optimal moves

Implement the method winning efficiently using dynamic programming.
Implement the class in a file graphgame.py according to the following template:
"""


class GraphGame:
    def __init__(self, n):
        # TODO
        pass

    def add_link(self, a, b):
        # TODO
        pass

    def winning(self, x):
        # TODO
        pass

if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3, 4)
    g.add_link(1, 4)
    g.add_link(4, 5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3, 1)
    g.add_link(4, 6)
    g.add_link(6, 5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False