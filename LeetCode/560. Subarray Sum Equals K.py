from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        d=defaultdict(int)
        d[0] = 1
        s=0
        ans = 0

        for i,val in enumerate(nums):
            s+=val
            ans += d[s-k]
            
            d[s] += 1
            # print(d,i)
            
        # print(d)
        return ans
        
nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums, k))