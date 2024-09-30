""" Description:
You are given an n*m grid that represents a map of a house. Each square is either floor (.) or wall (#), and all squares along the edges of the grid are wall.
Two floor squares belong to the same chamber if they are adjacent on the same row or column. How many chambers are there?
You may assume that 1 <= n, m <= 20.
In a file chambers.py, implement a function count that returns the number of chambers.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3