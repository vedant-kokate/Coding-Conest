from math import ceil, log
from heapq import heappush,heappop
from collections import defaultdict
class Solution:
    def maximumRobots(self, ct, rc, budget: int) -> int:
        def check(k):
            # print(k)
            deleted=defaultdict(int)
            heap=[]
            sum_=0
            for i in range(k):
                heappush(heap, -ct[i])
                sum_ += rc[i]
            val=heappop(heap)
            # print(-val,sum_)
            cost = -val + sum_*k
            if cost<=budget:
                # print(cost,k)
                return True 
            print(cost)
            heappush(heap, val)
            for i in range(k,len(ct)):
                deleted[ct[i-k]] += 1
                heappush(heap, -ct[i])
                val = -heappop(heap)

                while deleted[val]>0:
                    deleted[val] -= 1
                    val=-heappop(heap)
                heappush(heap, -val)
                sum_+=rc[i]
                sum_-=rc[i-k]
                cost = val + k*sum_
                print(cost)
                if cost<=budget:
                    # print(cost,k)
                    return True 
            return False
        
        n=len(rc)
        # print(check(4))
        l,h,ans=1,n,0 
        while l<=h:
            print(l,h)
            mid = (l+h)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                h=mid-1
        
        return ans

chargeTimes =[10,1,1,1]


runningCosts = [1,1,1,1]
# 19
budget = 26
print(Solution().maximumRobots(chargeTimes, runningCosts, budget))

