class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        catch = {}
        def dfs(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            
            match = i<len(s) and (s[i] ==p[j] or p[j]=='.')
            if j+1<len(p) and p[j+1]=='*':
                catch[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))
                return catch[(i,j)]
            if match:
                catch[(i,j)] = dfs(i+1,j+1)
                return catch[(i,j)]
            catch[(i,j)] = False
            return catch[(i,j)]
        return dfs(0,0)
        
s = "aab"
p = "c*a*b"

print(Solution().isMatch(s, p))