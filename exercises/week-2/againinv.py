""" Description:
Your task is to create a list containing the numbers 1 ... n so that the number of inversions is exactly k.
You may assume that n <= 100 and that k is chosen so that a solution exists. Any valid solution is acceptable.
In a file againinv.py, implement a function create that returns the desired list.

A pair of indices (i,j) is an inversion if i<j and the element at index i on the list is greater than the element at index j.
"""


def create(n, k):
    my_list = list(range(1, n + 1))
    inv_counter = 0

    if inv_counter == k:
        return my_list
    
    for i in range(n):
        for j in range(i + 1, n):
            if inv_counter == k:
                return my_list
            
            tmp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = tmp
            inv_counter += 1
    
    return my_list

if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(3, 3)) # esim. [3,2,1]