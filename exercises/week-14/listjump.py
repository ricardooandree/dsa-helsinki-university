""" Description:
You are given a list of n positive integers. You start at the beginning of the list and your goal is to reach the end of the list.
When you are at a value x, you can jump x positions to the right or to the left.
However, you cannot make a jump that would take you outside the list. You want to reach the end of the list with the smallest possible total length of the jumps.
You may assume that that n is at most 10^5. The algorithm should be efficient in all cases.
In a file listjump.py, implement a function calculate that returns the smallest total length of the jumps, or -1 if there is no way to reach the end of the list.
"""

""" Explanation:
Explanation: Given the list [3,5,2,2,2,3,5],the best solution is to jump first 3 steps to the right, then 2 steps to the left, and finally 5 steps to the right.
The total length of the jumps is 3+2+5=10.
"""


def calculate(t):
    # TODO
    pass

if __name__ == "__main__":
    print(calculate([1, 1, 1, 1])) # 3
    print(calculate([3, 2, 1])) # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5])) # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32