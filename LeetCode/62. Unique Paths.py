class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem= {(m,n):1}
        def dfs(i,j):

            if (i,j) in mem:
                return mem[(i,j)]
            if not(0<=i<=m and 0<=j<=n):
                return 0
            path = dfs(i+1,j) + dfs(i,j+1)

            mem[(i,j)] = path

            return path
        ans = dfs(1,1)
        # print(mem)
        return ans
m,n = 30,70
print(Solution().uniquePaths(m, n))