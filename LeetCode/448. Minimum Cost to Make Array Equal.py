from time import time

import numpy as np

st=time()
class Solution:
    def minCost(self, a, cost):
        def f(x):
            ans=0
            for i in range(n):
                diff=abs(a[i]-x)
                ans += diff*cost[i]
            return ans

        l,h,n=min(a),max(a),len(a)
        final_ans=10**18
        while l<=h:
            if time()-st>1:
                exit()

            
            mid = (l+h)//2
            
            c1=f(mid)
            c2=f(mid+1)
            print(l,mid,h,c1,c2)
            if c1<c2:
                h=mid-1
            else:
                l=mid+1
            final_ans=min(final_ans,c1,c2)
        return final_ans

        
a =[735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
cost =[724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]
print(Solution().minCost(a, cost))
