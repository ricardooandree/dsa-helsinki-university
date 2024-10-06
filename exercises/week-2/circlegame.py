""" Description:
There is a circle of n players numbered 1,2,...,n. 
The players take turns in order around the circle, and every second player leaves the circle until the circle is empty. 
Your task is to determine the order in which the players leave.
You may assume that n is in the range 1 ... 100.
In a file circlegame.py, implement a function create that returns the order.
"""
"""
[1, 2, 3, 4, 5, 6, 7] - len = 7
[2, 4, 6]
[1, 3, 5, 7] - len = 4
[2, 4, 6, 1, 5]
[3, 7] - len = 2
[2, 4, 6, 1, 5, 3, 7]

"""

def create(n):
    if n == 1:
        return [1]
    
    players = list(range(1, n + 1))
    result = []
    i = 0
    skip = 1

    while len(result) != n:
        i = (i + 1) % n
        if players[i] is None:
            continue
        else:
            skip += 1

        if skip == 2:
            player = players[i]
            result.append(player)
            players[i] = None
            skip = 0

    return result

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]