#!/bin/python3

import math
import os
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    n,m=len(a),len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = a[i-1].islower() and dp[i-1][0]

    for j in range(1, m+1):
        for i in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif a[i-1].isupper():
                dp[i][j] = False
            elif a[i-1].upper() == b[j-1]:
                dp[i][j] = dp[i-1][j-1] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return "YES" if dp[-1][-1] else "NO"

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)
