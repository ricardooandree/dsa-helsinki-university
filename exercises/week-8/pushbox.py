""" Description:
You are in an n*m labyrinth in the square marked X, and your task is to push the box in the square B into the square Y. Each square is either floor (.) or wall (#), and all squares along the edges of the grid are wall.
You can push the box by walking against it, which puts you in the square of the box and moves the box one step forward in the direction of your movement. What is the smallest number of steps needed to push the box into the target square?
You may assume that 1 <= n,m <= 20. If there is no solution, return −1.
In a file pushbox.py, implement a function count that returns the smallest number of steps.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
    print(count(r)) # 18