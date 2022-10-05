class Solution:
    def solve(self, board) :
        """
        Do not return anything, modify board in-place instead.
        """
        def f(i,j,vis):
            stack = [(i,j)]
            v=set()
            v.add((i,j))
            while stack:
                i,j = stack.pop()
                
                if i==0 or i==n-1 or j==0 or j==m-1:
                    return False
                
                for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x,y = i+r,j+c
                    if (x,y) not in v and board[x][y]=='O':
                        stack.append((x,y))
                        v.add((x,y))
            for i,j in v:
                board[i][j] = 'X'
            vis |= v 
        
        
        n,m = len(board),len(board[0])
        vis=set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    f(i,j,vis)
                        
                    
board = [["X","X","X"],["X","O","X"],["X","X","X"]]
Solution().solve(board)
for i in board:
    print(i)