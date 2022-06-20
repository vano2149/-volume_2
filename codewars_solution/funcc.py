import sys
import math


length = int(input())
for i in range(length):
    number = int(input())
    even = []
    odd = []
    if i % 2 == 0:
        i = i * 3
        even.append(i)
    else:
        i = i * 5
        odd.append(i)
    print(even)
    print(odd)


