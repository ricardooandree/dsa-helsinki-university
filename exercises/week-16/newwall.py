""" Description:
You are given an n*n grid where each square is floor or wall. 
The top left and bottom right corners are always floor and cannot be changed. In the description of the grid, the character . stands for floor and the character # stands for wall.
You can move right or down in the grid. How many squares have to be changed into wall so that there is no route from the top left corner to the bottom right corner?
In a file newwall.py, implement a function count that returns the smallest number of squares to change.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2