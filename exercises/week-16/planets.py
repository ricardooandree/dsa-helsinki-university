""" Description:
The game has n planets numbered 1,2,...,n. A player starts at the planet 1 and wins the game by reaching the planet n.
The planets are connected by teleports. Each teleport is described by a pair (a,b), where a<b, and teleports a player from the planet a to the planet b.
You have successfully played the game through, but you want to prevent anyone else from winning the game. How many teleports do you need to remove from the game?
Implement a class Planets with the following methods:

add_teleport adds a teleport from the planet a to the planet b
calculate returns the minimum number of teleports to remove

Implement the class in a file planets.py according to the following template.
"""


class Planets:
    def __init__(self, n):
        # TODO
        pass

    def add_teleport(self, a, b):
        # TODO
        pass

    def calculate(self):
        # TODO
        pass

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1, 2)
    p.add_teleport(2, 5)
    print(p.calculate()) # 1
    p.add_teleport(1, 5)
    print(p.calculate()) # 2