""" Description:
You are given a list that contains n integers. Your task is to create a new list that contains the sums of all subsets of the original list in order from smallest to largest.
You may assume that 1 <= n <= 10. The algorithm should be efficient in all these cases.
In a file subsets.py, implement a function create that returns the list of subset sums.
"""


""" Explanation:
Explanation: The subsets of the list [1,2,3] are [], [1], [2], [3], [1,2], [1,3], [2,3] and [1,2,3]. The sums of these subsets are [0,1,2,3,3,4,5,6].
"""


def create(t):
    # TODO
    pass

if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]