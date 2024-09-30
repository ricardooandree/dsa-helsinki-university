""" Description:
Your task is to count how many substrings of a string contain the characters t, i, r and a in some order.
The time complexity of the algorithm should be O(n).
In a file sequences.py, implement a function count that returns the desired count.
"""


""" Explanation:
Explanation: For example, the string ritari has six desired substrings: itar, itari, rita, ritar, ritari and tari.
"""


def count(s):
    # TODO
    pass

if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4