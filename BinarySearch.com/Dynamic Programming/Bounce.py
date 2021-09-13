from collections import deque
class Solution:
    def solve(self, nums, k):
        n=len(nums)
        vis=[False]*n
        stack=deque()
        stack.append(k)

        while stack:
            cur=stack.popleft()
            if vis[cur]:
                continue

            vis[cur]=True

            right=nums[cur]+cur
            left=cur-nums[cur]
            
            if right<n and vis[right]==False:
                stack.append(right)
            if left>=0 and vis[right]==False:
                stack.append(left)

        return vis[-1]