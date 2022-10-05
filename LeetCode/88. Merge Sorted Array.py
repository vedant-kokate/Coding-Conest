class Solution:
    def merge(self, n1, m, n2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        ans = n1[:m] + n2
        ans.sort()
        n1[0:] = ans
n1 = [1,2,3,0,0,0]
m = 3
n2 = [2,5,6]
n = 3

Solution().merge(n1, m, n2, n)
print(n1)