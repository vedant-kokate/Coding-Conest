from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int):
        
        d=defaultdict(dict)
        def f(board,k,d,i,j):
            
            if k==0:
                temp=[]
                for _ in board:
                    temp.append("".join(_))
                # print(k,i,j)
                self.ans.append(temp)
                return
            while i<n:
                while j<n:
                    if i not in d['row'] and j not in d['col']:
                        if i-j not in d['d1'] and i+j not in d['d2']:
                            board[i][j]='Q'
                            d['row'][i],d['col'][j],d['d1'][i-j],d['d2'][i+j]=True,True,True,True 
                            
                            f(board,k-1,d,i,j+1)
                            
                            board[i][j]='.'
                            del d['row'][i]
                            del d['col'][j]
                            del d['d1'][i-j]
                            del d['d2'][i+j]
                    j+=1
                j=0
                i+=1
        board= [['.']*n for i in range(n)]
        self.ans=[]
        f(board,n,d,0,0)
        return self.ans
        

n=int(input())
sol = Solution().solveNQueens(n)
print(len(sol))