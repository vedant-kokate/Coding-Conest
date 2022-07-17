from bisect import bisect_left,bisect_right

class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
        l,r = bisect_left(a,target), bisect_right(a,target)-1
        if a==[]:
            return [-1,-1]
        if l==0 and a[0]!=target:
            return [-1,-1]
        
        if r==len(a)or l==len(a):
            return [-1,-1]
        if a[l]!=target:
            return [-1,-1]
        return [l,r]
nums = [5,7,7,8,8,10]
target = 6
print(Solution().searchRange(nums, target))