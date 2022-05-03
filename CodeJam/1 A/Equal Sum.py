import sys
input=sys.stdin.readline
import numpy as np
from heapq import heapify,heappop, heappush
from collections import defaultdict,deque
def f():return list(map(int,input().split()))

def knapSack(W, wt, n):
	K = [[0 for w in range(W + 1)]
			for i in range(n + 1)]

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(wt[i - 1]
				+ K[i - 1][w - wt[i - 1]],
							K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	res = K[n][W]

	# ans = []
	# w = W
	# for i in range(n, 0, -1):
	# 	if res <= 0:
	# 		break

	# 	if res == K[i - 1][w]:
	# 		continue
	# 	else:

	# 		ans.append(wt[i-1])

	# 		res = res - wt[i - 1]
	# 		w = w - wt[i - 1]

	return []



for _ in range(int(input())):
    n = int(input())
    if n==-1:
        exit()
    arr = []
    for i in range(min(n,30)):
        arr.append(2**i)

    for i in range(133,133+n-len(arr)):
        arr.append(i)
    print(*arr,flush=True)
    a = f()
    s1, s2 = sum(arr), sum(a)

    if s1==s2:
        print(*a,flush=True)
    elif s1>s2:
        ans = (s1-s2)//2
        for i in range(30):
            if ans%(2**i)==0:
                a.append(2**i)
        print(*a,flush=True)
    else:
        arr+=knapSack((s2-s1)//2, a, n)
        print(a,flush=True)
    