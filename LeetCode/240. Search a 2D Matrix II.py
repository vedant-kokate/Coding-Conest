class Solution:
    def searchMatrix(self, mat, target) -> bool:
        n,m = len(mat),len(mat[0])
        
        i,j = 0,m-1
        print(i,j)
        while 0<=i<n and 0<=j<m:
            print(i,j)
            if mat[i][j]==target:
                return True
            if mat[i][j]>target:
                j-=1
            else:
                i+=1
        return False
matrix = [[5]]
target = 5
print(Solution().searchMatrix(matrix, target))
from random import ra