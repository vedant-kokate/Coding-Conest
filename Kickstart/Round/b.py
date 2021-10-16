from heapq import heappush, heappop, heapify
import sys
from collections import defaultdict
input=sys.stdin.readline
def f():return list(map(int,input().split()))


class MaxHeap:
    def  __init__(self):
        self.h = []

    def append(self, item):
        item *= -1
        heappush(self.h, item)

    def pop(self):
        return heappop(self.h) * -1

    def pop_item(self, item):
        item *= -1
        idx = self.h.index(item)
        self.h[idx], self.h[-1] = self.h[-1], self.h[idx]
        self.h.pop()
        heapify(self.h)
    def k_sum(self,k):
        ans=0
        stack=[]
        for i in range(min(k,len(self.h))):
            stack.append(self.pop())
        # print('stack',stack)
        ans=sum(stack)
        while stack:
            x=stack.pop()
            self.append(x)
        return ans
        

for _ in range(int(input())):
    D,n,k=f()
    a=[]
    d=defaultdict(list)
    for i in range(n):
        hi,si,ei=f()
        si=si-1
        ei=ei
        d[si].append(hi)
        d[ei].append(-hi)


    # print(d)
    ans=-1
    heap=MaxHeap()
    for i in range(D):
        if len(d[i])>0:
            for adding in d[i]:
                
                if adding>0:
                    heap.append(adding)
                    # heappush(heap,-adding)
                   
                else:
                    heap.pop_item(-adding)

        
        ans=max(ans,heap.k_sum(k))
        # print(i,ans)
    print(f"Case #{_+1}: {ans}")
