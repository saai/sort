#!/usr/bin/env python
import random
from timeit import default_timer as timer

def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        k = a[i]
        j = i-1
        while j >= 0 and a[j] > k:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k
    return a

def merge (a, left, right):
    i = 0
    j = 0
    k = 0
    ll = len(left)
    lr = len(right)
    while i < ll and j < lr:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else :
            a[k] = right[j]
            j += 1
        k += 1
    # copy rest of left
    while i < ll :
        a[k] = left[i]
        i += 1
        k += 1
    # copy rest of right
    while j < lr :
        a[k] = right[j]
        j += 1
        k += 1

def merge_sort(a):
    p = 0
    r = len(a)
    if r <= 1:
        return 
    m = (p+r)/2
    left = a[:m]
    right = a[m:r]
    merge_sort(left)
    merge_sort(right)
    merge(a,left,right)      



def shell_sort():
    pass

def quick_sort():
    pass

def count_sort():
    pass

def radix_sort():
    pass

def random_int(max, n):
    return random.sample(xrange(max),n)

def judge(a):
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return 0, i 
    return 1
   
def test():
    max_v = 2**32 -1 
    max_n = 10**2
    a = random_int(max_v, max_n)
    print a 
    # insert_sort(a)
    merge_sort(a)
    print judge(a)


test()

