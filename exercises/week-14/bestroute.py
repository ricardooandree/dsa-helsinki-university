""" Description:
Bitland has n cities that initially have no connecting roads.
Your task is to design a class that supports adding a road between two cities and finding the shortest route between two cities.
The class should have the following methods:

    add_road adds a road of length x between the cities a and b
    find_route returns the length of the shortest route between two cities a
    and b (or -1 if there is no route)

The cities are numbered 1,2,...,n. All the roads go both directions and thus the order of the two cities in the calls makes no difference.
In a file bestroute.py, implement a class BestRoute according to the following template.
"""


class BestRoute:
    def __init__(self, n):
        # TODO
        pass

    def add_road(self, a, b, x):
        # TODO
        pass

    def find_route(self, a, b):
        # TODO
        pass

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3)) # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3)) # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3)) # 3