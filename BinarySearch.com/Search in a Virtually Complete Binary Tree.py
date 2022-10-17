from collections import defaultdict
class Solution:
    def solve(self, a, k):
        st=0
        d=defaultdict(int)
        max_rep = 0
        for e,val in enumerate(a):
            d[val]+=1
            max_rep=max(max_rep,d[val])
            # print(max_rep)
            while max_rep+k<e-st+1:
                d[a[st]]-=1
                st+=1
        return e-st+1



        return end - start + 1
nums = [7, 5, 5, 3, 2, 5, 5]
k = 0
print(Solution().solve(nums, k))