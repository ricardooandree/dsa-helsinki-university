""" Description:
You are given data about customers arriving to and departing from a restaurant in the same way as on the course material.
Your task is to find out what is the longest time that the restaurant is empty between the departure of a customer and the arrival of another customer.
The time complexity of the algorithm should be O(nlog n).
In a file restaurant.py, implement a function find that returns the longest time.
"""


def find(a, d):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1, 6], [2, 9])) # 4
    print(find([1, 2, 3], [2, 3, 4])) # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9])) # 1
    print(find([1, 10**9], [2, 10**9+1])) # 999999998 