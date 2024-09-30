""" Description:
You are given a bit string with n characters. In each step, you may erase two adjacent bits that are different. How many ways there are to erase all bits?
For example, when the bit string is 101100, there are 5 possible ways:

\underline{10}1100 -> 1\underline{10}0 -> \underline{10} -> (empty)
1\underline{01}100 -> 1\underline{10}0 -> \underline{10} -> (empty)
101\underline{10}0 -> \underline{10}10 -> \underline{10} -> (empty)
101\underline{10}0 -> 1\underline{01}0 -> \underline{10} -> (empty)
101\underline{10}0 -> 10\underline{10} -> \underline{10} -> (empty)

You may assume that 1 <= n <= 30. The algorithm should be efficient in all these cases.
In a file biterase.py, implement a function count that returns the number of ways to erase all bits.
"""


def count(s):
    # TODO
    pass

if __name__ == "__main__":
    print(count("1001")) # 2
    print(count("1100")) # 1
    print(count("101100")) # 5
    print(count("11001")) # 0
    print(count("01110100100110")) # 6027