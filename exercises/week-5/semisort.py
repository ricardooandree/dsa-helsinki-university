""" Description:
A list contains the numbers 1 \dots n in some order. In each step, you can swap two adjacent numbers. Your task to order the list so that all the numbers in the first half are smaller than all the numbers in the last half. What is the smallest number of swaps you need?
The time complexity of the algorithm should be O(n). You may assume that n is even.
In a file semisort.py, implement a function solve that returns the smallest number of swaps.
"""

""" Explanation:
Explanation: On the list [2,1,4,3], the numbers in the first half, 2 and 1, are already smaller than the numbers 4 and 3 in the last half.
The list [5, 3, 4, 1, 6, 2] needs at least 6 swaps. Here is one optimal sequence of swaps: [5, 3, 4, 1, 6, 2] -> [5, 3, 4, 1, 2, 6] -> [3, 5, 4, 1, 2, 6] -> [3, 5, 1, 4, 2, 6] -> [3, 1, 5, 4, 2, 6] -> [3, 1, 5, 2, 4, 6] -> [3, 1, 2, 5, 4, 6]
"""


def solve(t):
    # TODO
    pass

if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15