class Solution:
    def rotate(self, a) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in a:
            print(i)
        print()
        n,m = len(a),len(a[0])
        M = [[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                M[i][j] = a[n-1-j][i]

        for i in range(n):
            for j in range(m):
                a[i][j] = M[i][j]
        

        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(matrix))

for i in matrix:
    print(i)
# print(matrix)