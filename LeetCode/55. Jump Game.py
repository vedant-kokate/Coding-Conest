from collections import deque
class Solution:
    def canJump(self, a) -> bool:
        n=len(a)
        max_ = 0
        for i, val in enumerate(a):
            if i<=max_:
                max_ = max(a[i]+i,max_)
        return max_>=n-1
        
            

nums = [2,5,0,0]
print(Solution().canJump(nums))