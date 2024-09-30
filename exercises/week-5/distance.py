""" Description:
A list contains n integers in the range 1\dots k. We want to add another integer in the range 1\dots k to the list so that the distance of the new number to the nearest old number is as large as possible. What is this distance?
The time complexity of the algorithm should be O(n \log n).
In a file distance.py, implement a function find that returns the maximal distance.
"""


""" Explanation:
Explanation: In the first case, the result is 3, because we can add the number 5 or 6 so that the distance (to 2 or 9) is 3. It is not possible to add a number so that the distance is 4 or more.
"""


def find(t, k):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970