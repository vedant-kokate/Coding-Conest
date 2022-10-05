class Solution:
    def exist(self, board, word: str):
        def f(i,j,idx):
            # print(i,j,idx)
            if idx==len(word):
                return True
            ops = [(-1,0),(1,0),(0,-1),(0,1)]
            for x,y in ops:
                X = x+i
                Y = y+j
                ans = False
                # print(X,Y,word[idx])
                if 0<=X<len(board) and 0<=Y<len(board[0]) and board[X][Y]==word[idx]:
                    temp = board[i][j]
                    board[i][j] = '#'
                    ans = f(X,Y,idx+1)
                    board[i][j] = temp
                if ans: return ans
            
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    ans = f(i,j,1)
                    if ans: return ans
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(Solution().exist(board, word))   
            