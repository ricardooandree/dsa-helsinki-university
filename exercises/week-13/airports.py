""" Description:
Bitland has n airports that initially have no flights between them.
Your task is to implement a class that supports adding flight connections between airports, and checking if every airport can be reached from all other airports (either directly or indirectly via other airports).
Implement a class Airports with the following methods:

add_link adds a one-directional flight connection from an airport a to an airport b
check reports if every airport can be reached from all other airports

Implement the class in a file airports.py according to the following template:
"""


class Airports:
    def __init__(self, n):
        # TODO
        pass

    def add_link(self, a, b):
        # TODO
        pass

    def check(self):
        # TODO
        pass

if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check()) # False
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check()) # False
    a.add_link(5, 1)
    print(a.check()) # True