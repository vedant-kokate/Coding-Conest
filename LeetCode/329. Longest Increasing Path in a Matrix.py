from heapq import heapify,heappop,heappush
class Solution:
    def longestIncreasingPath(self, matrix):
        heap = []
        n,m = len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                heappush(heap, (matrix[i][j],i,j))

        dp = [[1]*m for i in range(n)]
        while heap:
            val,i,j = heappop(heap)
            for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y = r+i, j+c
                if 0<=x<n and 0<=y<m and matrix[x][y]>matrix[i][j]:
                    dp[x][y] = max(dp[x][y],dp[i][j] + 1)
        ans = 0
        
        for i in dp:
            # print(i)
            for j in i:
                ans = max(ans,j)
        return ans

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(Solution().longestIncreasingPath(matrix))