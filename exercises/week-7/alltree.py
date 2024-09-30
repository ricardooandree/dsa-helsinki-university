""" Description:
Count how many trees have n nodes and k leaves.
For example, when n=4 and k=2, the trees are:

(alltree.png)

Two trees are similar if the roots have the same number of children and each subtree is similar when we go through the children from left to right.
You may assume that 1 <= n <= 10. Your solution should be efficient in all of these cases.
In a file alltree.py, implement a function count that returns the desired count.
"""


def count(n, k):
    # TODO
    pass

if __name__ == "__main__":
    print(count(4, 1)) # 1
    print(count(4, 2)) # 3
    print(count(4, 3)) # 1
    print(count(4, 4)) # 0
    print(count(10, 4)) # 1176