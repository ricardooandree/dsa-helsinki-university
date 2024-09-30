""" Description:
Report the time complexity of each of the following algorithms. The correct answer in each case is one of the following: O(1), O(n), O(n^2), O(n^3), O(n^4).
When you press the submit button, your answers are checked, and you can then change your answers. When all answers are correct, you get a point for the exercise.
"""

# Algorithm 1 - Time complexity: O(n)
def algo1(n):
    result = 0
    for i in range(n):
        result += i
    return result


# Algorithm 2 - Time complexity: O(n)
def algo2(n):
    result = 0
    for i in range(n):
        result += i
    for i in range(n):
        result -= i
    return result


# Algorithm 3 - Time complexity: O(1)
def algo3(n):
    return 5*n**2


# Algorithm 4 - Time complexity: O(n)
def algo4(n):
    result = 0
    while n > 0:
        n -= 1
        result += 2
    return result


# Algorithm 5 - Time complexity: O(n^2)
def algo5(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i*j
    return result


# Algorithm 6 - Time complexity: O(1)
def algo6(n):
    result = 0
    for i in range(10):
        result += n
    return result


# Algorithm 7 - Time complexity: O(1)
def algo7(n):
    result = n
    for i in range(100):
        for j in range(100):
            result -= 1
    return result


# Algorithm 8 - Time complexity: O(1)
def algo8(n):
    return 1
    result = 0
    for i in range(n):
        result += 1