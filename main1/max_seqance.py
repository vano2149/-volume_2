"""
The maximum sum subarray problem consists in finding the maximum sum 
of a contiguous subsequence 
in an array or list of 
integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]


Easy case is when the list is made up of only positive numbers 
and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. 
Note that the empty list or array is also a valid sublist/subarray.
"""

def max_sequence(arr):
    lis1 = []
    lis2 = []
    for i in arr:
        if i < 0:
            lis1.append(i)
        print(sum(lis1))
    for k in arr:
        if k > 0:
            lis2.append(k)
        print(sum(lis2))
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])