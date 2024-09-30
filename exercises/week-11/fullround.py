""" Description:
Initially the contents of the list are [1,2,3,...,n]. In each step, you take the first two elements of the list and move them to the end of the list in reverse order. How many steps is needed until the original contents of the list are restored?
Your task is to design an algorithm that is efficient even for very large values of n. The time complexity of the algorithm should be O(1).
In a file fullround.py, implement a function count that returns the number of steps.
"""


def count(n):
    # TODO
    pass

if __name__ == "__main__":
    print(count(2)) # 2
    print(count(5)) # 6
    print(count(31)) # 240
    print(count(1234567)) # 381038919372