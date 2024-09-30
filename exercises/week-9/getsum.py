""" Description:
A list contains the integers 1 \dots n. How many ways can you choose k numbers from the list so that their sum is x?
You may assume that 1 <= n <= 10 and that 1 <= k <= n. The algorithm should be efficient in all these cases.
In a file getsum.py, implement a function count that returns the desired count.
"""


""" Explanation:
Explanation: When n=8, k=3 and x=12, the answer is 6. Here the list is [1,2,3,4,5,6,7,8] and the possible ways are [1,3,8], [1,4,7], [1,5,6], [2,3,7], [2,4,6] and [3,4,5].
"""


def count(n, k, x):
    # TODO
    pass

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16