""" Description:
Your task is to count the nodes that have the same number of nodes in each child subtree.

In a file subtrees.py, implement a function count that returns the desired count.
"""


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    # TODO
    pass

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 8