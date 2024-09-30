""" Description:
You are given two water containers with the capacities of a and b liters, and your task is to measure x liters using the containers.
Initially the containers are empty and they have no measuring scale.
In each step, you can fill or empty one of the containers or pour water from one container to the other, but only so that one of the containers becomes full or empty, because otherwise the measurement would not be exact.
What is the smallest amount of water needed to move in order to measure exactly x liters into the first container? For example when a=5, b=4 and x=2, the smallest amount is 22 liters. Here is one optimal solution:

1-Fill the first container (5 liters of water moved)
2-Pour from the first container to the second one (4 liters of water moved)
3-Empty the second container (4 liters of water moved)
4-Pour the contents of the first container into the second one (1 liter of water moved)
5-Fill the first container (5 liters of water moved)
6-Pour from the first container to the second one (3 liters of water moved)

You may assume that 1 <= a,b <= 500 and that 1 <= x <= a. The algorithm should be efficient in all these cases. If there is no solution, the answer should be -1. 
In a file water.py, implement a function count that returns the smallest amount of water to move.
"""


def count(a,b,x):
    # TODO
    pass

if __name__ == "__main__":
    print(count(5, 4, 2)) # 22
    print(count(4, 3, 2)) # 16
    print(count(3, 3, 1)) # -1
    print(count(10, 9, 8)) # 46
    print(count(123, 456, 42)) # 10530