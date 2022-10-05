from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        def compare(x,y):
            a=int(x+y)
            b=int(y+x)
            if a>b:
                return 1
            else:
                return -1


        nums =[str(x) for x in nums]
        nums.sort(key=cmp_to_key(compare),reverse=True)
        ans = "".join(nums)
        i=0
        while i<len(ans)-1 and ans[i]=='0':
            i+=1
        return ans[i:]

nums = [0,0]
print(Solution().largestNumber(nums))