""" Description:
A warehouse contains n boxes, each with a given weight. How many boxes can be packed into a van, when the maximum load of the van is x?
The time complexity of the algorithm should be O(nlog n).
In a file packbox.py, implement a function solve that returns the maximum number of boxes.
"""


""" Explanation:
Explanation: In the first example, any two boxes fit in the van. In the second example, the three boxes packed into the van could be, for example, the three first boxes with a total weight of 10.
In the third example, no box can be loaded into the van since all of them weigh more than 1.
"""


def solve(t, x):
    # TODO
    pass

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1