""" Description:
You are given an n*m grid, where each square contains a positive integer. Your goal is to travel from the the top left-hand corner to the bottom right-hand corner.
In each step, you can move up, down, left or right. However, you cannot move outside the grid.
The cost of your route is the sum of the values encountered on the route. What is the smallest possible cost of a route?
In a file gridpath.py, implement a function count that returns the smallest cost of a route.
"""

""" Explanation:
Explanation: The best route is to move first two steps to the right, then two steps down, and finally one step to the right. The cost of the route is 2+1+4+7+1+2=17.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = [[2, 1, 4, 8],
         [3, 8, 7, 2],
         [9, 5, 1, 2]]
    print(count(r)) # 17