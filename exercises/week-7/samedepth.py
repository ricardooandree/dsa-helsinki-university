""" Description:
Your task is to check if every leaf in a given tree has the same depth.

In a file samedepth.py, implement a function check that reports if all leaves have the same depth.
"""


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check(node):
    # TODO
    pass

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3)]), Node(4, [Node(5), Node(6)])])

    print(check(tree1)) # False
    print(check(tree2)) # True