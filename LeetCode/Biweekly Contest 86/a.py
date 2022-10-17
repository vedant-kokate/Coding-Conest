from collections import defaultdict,deque
class Solution:
    def findSubarrays(self, nums) -> bool:
        d=defaultdict(int)
        n=len(nums)
        for i in range(n-1):
            s=nums[i]+nums[i+1]
            d[s]+=1
            if d[s]>1:
                return True
            
        return False

nums = [0,0,0]
print(Solution().findSubarrays(nums))
