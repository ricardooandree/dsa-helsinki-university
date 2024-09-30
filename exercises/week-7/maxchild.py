""" Description:
Your task is to find out what is the maximum number children of any node in a given tree.

In a file maxchild.py, implement a function count that returns the maximum child count.
"""


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    # TODO
    pass

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3), Node(4)])])

    print(count(tree1)) # 3
    print(count(tree2)) # 2