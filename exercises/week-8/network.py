""" Description:
A network consists of n computers that initially have no connecting links between them. Your task is to implement a class that can be used for adding a link between two computers and for finding the shortest route between two computers.
You may assume that there are at most 50 computers and that the methods of the class are called at most 100 times.
In a file network.py, implement a class Network with the following methods:

    - constructor with the number of computers as a parameter
    - add_link adds a link between two computers
    - best_route returns the number of links on the shortest route connecting two computers (or -1 if there is no route) 
"""


class Network:
    def __init__(self, n):
        # TODO
        pass

    def add_link(self, a, b):
        # TODO
        pass

    def best_route(self, a, b):
        # TODO
        pass

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5)) # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5)) # 2