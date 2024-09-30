""" Description:
Implement a class Median with the following methods:

add(x): add the number x to the list
median(): return the median of the list, i.e., the middle element when ordered by value (if the length of the list is even, return the smaller of the two middle elements)

Both methods should be efficient (time complexity O(1) or O(log n)).
In a file median.py, implement a class Median according to the following template.
"""

""" Explanation:
Explanation: In the example, the lists are [1], [1,2], [1,2,1], [1,2,1,3], [1,2,1,3,3] and their medians are 1, 1, 1, 1 and 2.
"""


class Median:
    def __init__(self):
        # TODO
        pass

    def add(self, x):
        # TODO
        pass

    def median(self):
        # TODO
        pass

if __name__ == "__main__":
    m = Median()
    m.add(1)
    print(m.median()) # 1
    m.add(2)
    print(m.median()) # 1
    m.add(1)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 2