#!/usr/bin/env python3
import random
import math
from timeit import default_timer as timer

def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# gap = n/(2^i)
def shell_sort(a):
    n = len(a)
    gap = round(n/2)
    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i-gap 
            while j >= 0 and a[j] > key: 
                a[j+gap] = a[j]
                j -= gap  
            a[j+gap] = key 
            # other style
            # j = i 
            # while j >= gap and a[i - gap] > key:
            #     a[j] = a[j-gap]
            #     j -= gap
            # a[j] = key

        gap  = round(gap/2)
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
    return a 

def partition(a, p, r):
    i = p-1
    j = p
    key = a[r]
    for j in range(p, r):
        if a[j] <= key:
            i += 1 
            a[i],a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def quick_sort(a, p, r):
    if p < r: 
        q = partition(a, p, r)
        quick_sort(a, p, q-1) # NOTICE q-1 not q
        quick_sort(a, q+1,r)  # NOTICE q+1 not q
    return a 

def bit_count_sort(a, b, pss, r):
    n = len(a)
    mask = 1
    # mask 为二进制数 r个1
    for i in range(1, r):
        mask |= (1<<i)
    # print ('mask', mask)
    c = [0]*(mask+1) # 每一位都有 mask+1 种选择
    move = (pss*r)
    # print('move', move)
    
    bit_v = mask<<move
    # print ('bit_v', bit_v)

    # print ('a', a)
    aa = list(map(lambda x : (x&bit_v)>>move, a)) # loc bit value

    # print ('aa', aa)
    # c[i] contains number of i 
    for i in range(0, n):
        c[aa[i]] += 1

    # print ('c', c)
    # c[i] contains number of elements <= i
    for i in range(1,mask+1):
        c[i] += c[i-1]

    # print ('c', c)

    for j in range(n-1, -1, -1):
        b[c[aa[j]]-1] = a[j]
        c[aa[j]] -= 1
    # print (b)

    return b 


def radix_sort(a, bit):
    n = len (a)
    tmpa = [0]*n
    r = round(math.log2(n))
    # print('r' , r)
    pss = math.ceil(1.0*bit/r)
    # print('passes', pss)
    flag = 0
    for i in range(0,pss):
        if flag == 0:
            bit_count_sort(a,tmpa, i, r)
        else:
            bit_count_sort(tmpa, a, i, r)
        flag ^= 1

    if flag == 1:
        return tmpa
    else:
        return a 


def random_int(max, n):
    return random.sample(range(0,max),n)

def judge(a):
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return 0, i 
    return 1

def judge_same(a, b):
    n1= len(a)
    n2 = len(b)
    if n1 != n2:
        return 0
    for i in range(0, n1):
        if a[i] != b[i]:
            return 0, i
    return 1
   
def test():
    max_bit = 32
    max_v = 2**max_bit -1 
    max_n = 10**2
    a = random_int(max_v, max_n)
    n = len(a)
    # insert_sort(a)
    # merge_sort(a)
    # quick_sort(a, 0, n-1)
    # shell_sort (a)
    a = radix_sort(a, max_bit)
    print(a)
    print(judge(a))

test()

