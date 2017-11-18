#!/bin/python3

import sys
import bisect

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    item = int(input().strip())
    bisect.insort(a, item)
    pos = len(a) // 2
    result = float(a[pos])
    if len(a) % 2 == 0:
        result += a[pos - 1]
        result /= 2
    print(result)
