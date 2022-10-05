class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        ans = ""
        for i in range(len(a[0])):
            flag = True
            for j in range(len(a)):
                if i>=len(a[j]) or a[j][i]!=a[0][i]:
                    flag=False
                    return ans
            if flag:
                ans +=a[0][i]
                
        return ans
                    