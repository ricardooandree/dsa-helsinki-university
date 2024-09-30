""" Description:
You are given an n*m labyrinth and your task is to go from the square A to the square B.
Here the labyrinth has two kinds of walls: a wall at the border of the labyrinth is marked with # as before but internal walls are marked with *.
You can break an internal wall to open new routes through the labyrinth.
What is the smallest number of walls that you need to break in order to reach your goal? 
In a file breakwall.py, implement a function count that returns the smallest number of walls to break.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2