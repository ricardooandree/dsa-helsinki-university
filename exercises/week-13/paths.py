""" Description:
Your task is to construct a directed acyclic graph with 100 nodes and exactly x different paths from the node 1 to the node 100.
The graph can have at most 1000 edges and every edge must be different.
For example, when x=5, one possible solution consists of the edges 

(1,3),(1,5),(2,100),(3,2),(3,100),(5,2),(5,3)

In this case, the paths are:

1 -> 3 -> 100
1 -> 3 -> 2 -> 100
1 -> 5 -> 2 -> 100
1 -> 5 -> 3 -> 100
1 -> 5 -> 3 -> 2 -> 100

You may assume that x is an integer in the range 1 ... 10^9. You can construct any graph that satisfies the conditions.
In a file paths.py, implement a function create that returns the graph as a list of edges. 
"""


def create(x):
    #TODO
    pass

if __name__ == "__main__":
    print(create(2)) # esim. [(1,2), (1,100), (2,100)]
    print(create(5))
    print(create(10))
    print(create(123456789))