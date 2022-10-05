class Solution:
    def numIslands(self, grid ) -> int:
        
        n,m = len(grid),len(grid[0])
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    stack=[(i,j)]
                    grid[i][j]='2'
                    while stack:
                       
                        x,y =stack.pop()
                        for r,c in [(1,0),(0,1),(-1,0),(0,-1)]:
                            X=x+r
                            Y=y+c
                            if 0<=X<n and 0<=Y<m and grid[X][Y]=='1':
                                stack.append((X,Y))
                                grid[X][Y] = 2
                    count+=1
        return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))