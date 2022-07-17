class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        # print("row")
                        return False
                if board[j][i]!=".":
                    if board[j][i] not in col:
                        col.add(board[j][i])
                    else:
                        # print("col")
                        return False
                
            
        for i in range(3):
            for j in range(3):
                box = set()
                for x in range(3):
                    for y in range(3):
                         if board[i*3+x][j*3+y]!=".":
                                if board[i*3+x][j*3+y] not in box:
                                    box.add(board[i*3+x][j*3+y])
                                else:
                                    # print(i*3+x,j*3+y,"box",box)
                                    return False
                # print(box)
        return True
            
            
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))