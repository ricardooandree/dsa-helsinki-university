""" Description:
The course material includes two different ways to implement the function count_even:

Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.
In this exercise, you get a point automatically when you submit the test results and the code that you used.
"""
import random
import time

# Implementation 1
def count_even_one(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# Implementation 2
def count_even_two(numbers):
    return sum(x % 2 == 0 for x in numbers)


# Implementation 1 run time: 0.81 s
# Implementation 2 run time: 1.01 s

if __name__ == "__main__":
    random.seed(1337)
    numbers = [random.randint(1, 10**7) for _ in range(10**7)]

    start_time = time.time()
    result = count_even_one(numbers)
    end_time = time.time()

    print("time one: ", round(end_time - start_time, 2), "s")

    start_time = time.time()
    result = count_even_two(numbers)
    end_time = time.time()

    print("time two: ", round(end_time - start_time, 2), "s")