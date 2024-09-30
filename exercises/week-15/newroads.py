""" Description:
Bitland has n cities that initially have no connecting roads. The goal is to connect all cities to each other using roads.
You are given a set of possible roads and the construction cost for each road. What is the smallest cost of a road network that has a route between every pair of two cities?
Implement a class NewRoads with the following methods:

add_road adds the possibility of a road of cost x between the cities a and b 
min_cost returns the smallest cost of connecting all cities (or −1 if it is not possible to connect all cities)

Implement the class in a file newroads.py according to the following template:
"""


class NewRoads:
    def __init__(self, n):
        # TODO
        pass

    def add_road(self, a, b, x):
        # TODO
        pass

    def min_cost(self):
        # TODO
        pass

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1, 2, 2)
    n.add_road(1, 3, 5)
    print(n.min_cost()) # -1
    n.add_road(3, 4, 4)
    print(n.min_cost()) # 11
    n.add_road(2, 3, 1)
    print(n.min_cost()) # 7