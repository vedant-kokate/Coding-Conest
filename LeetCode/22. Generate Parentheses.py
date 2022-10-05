class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs(s,val):
            if len(s)==2*n:
                ans.append(s)
                return
            if val<2*n-len(s):
                dfs(s+'(', val+1)
            if val>0:
                dfs(s+')',val-1)
        dfs("",0)
        return ans
    