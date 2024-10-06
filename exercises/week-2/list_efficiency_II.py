""" Description:
Implement a test, where the numbers 1,2,...,n are added to the end of the list one at a time. Then the first element of the list is deleted n times.
Implement the test with n=10^5. Make two time measurements: How much time it takes to do all the additions, and how much time to do all the deletions.
In this task you get a point automatically when you fill in your measurement results and the code used in the test, and press the submit button.
"""
import time

# Time for additions: 0.01 s
# Time for deletions: 1.58 s
# The code you used in the test:
if __name__ == "__main__":
    n = 10**5
    numbers = []

    start_time = time.time()
    for i in range(1, n + 1):
        numbers.append(i)
    end_time = time.time()

    add_time = round(end_time - start_time, 2)

    start_time = time.time()
    for _ in range(1, n + 1):
        numbers.pop(0)
    end_time = time.time()

    delete_time = round(end_time - start_time, 2)

    print(f"Time for additions: {add_time} s")
    print(f"Time for deletions: {delete_time} s")