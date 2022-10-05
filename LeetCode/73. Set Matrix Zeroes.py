class Solution:
    def setZeroes(self, mat) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col = {},{}
        n,m = len(mat),len(mat[0])
        for i in mat:
            print(i)
        print()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    row[i]=True
                    col[j]=True
                    
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    mat[i][j] = 0
        for i in mat:
            print(i)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
ans = Solution().setZeroes(matrix)