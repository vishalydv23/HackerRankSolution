#!/bin/python3
import sys

SENTINEL = 10**8

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left, right = a[0:mid], a[mid:]
        merged = merge(merge_sort(left), merge_sort(right))
        return merged
    else:
        return a
    
def merge(_a, _b):
    global cnt
    a = _a + [SENTINEL]
    b = _b + [SENTINEL]
    res = []
    i, j = 0, 0
    for _ in range(len(_a) + len(_b)):
        if a[i] > b[j]:
            res += [b[j]]
            j += 1
            cnt += len(_a) - i
        else:
            res += [a[i]]
            i += 1
    return res

def countInversions(arr):
    # Complete this function
    global cnt
    cnt = 0
    merge_sort(arr)
    return cnt

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
