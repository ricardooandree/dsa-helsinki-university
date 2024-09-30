""" Description:
Bitland has n cities that initially have no connecting roads. Your task is to implement a class that can be used for adding a road between two cities and for finding out if there is a route between two cities.
You may assume that there are at most 50 cities and that the methods of the class are called at most 100 times.
In a file cities.py, implement a class Cities with the following methods:

    - constructor with the number of cities as a parameter
    - add_road adds a road between two cities
    - has_route checks if two cities are connected by route
"""


class Cities:
    def __init__(self, n):
        # TODO
        pass

    def add_road(self, a, b):
        # TODO
        pass

    def has_route(self, a, b):
        # TODO
        pass

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True