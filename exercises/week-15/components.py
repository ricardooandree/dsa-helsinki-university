""" Description:
Bitland has n cities that initially have no connecting roads. Two cities belong to the same component if it is possible travel between them using roads.
Implement a class that supports adding a road between two cities and counting the number of components formed by the cities.
Implement a class Components with the following methods:

add_road adds a road between two cities
count returns the number of components

Implement the class in a file components.py according to the following template:
"""

class Components:
    def __init__(self, n):
        # TODO
        pass

    def add_road(self, a, b):
        # TODO
        pass

    def count(self):
        # TODO
        pass

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count()) # 3
    c.add_road(2, 3)
    print(c.count()) # 3
    c.add_road(4, 5)
    print(c.count()) # 2