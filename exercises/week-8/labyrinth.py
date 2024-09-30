""" Description:
You are given an n*m grid that represents a labyrinth. Your task is to determine the length of the shortest route from the square A to the square B. Each square is either floor (.) or wall (#), and all squares along the edges of the grid are wall.
You may assume that 1 <= n,m <= 20. If there is no path, return −1.
In a file labyrinth.py, implement a function count that returns the length of the shortest route.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7