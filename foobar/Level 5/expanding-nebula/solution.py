from itertools import combinations,permutations
from collections import defaultdict
# MOD = 
def change(dupli,var,i):
    dupli[0][i] = var[0]
    dupli[0][i+1] = var[1]
    dupli[1][i] = var[2]
    dupli[1][i+1] = var[3]

def check(var,i,dupli):
    if dupli[0][i]!=-1 and dupli[0][i]!=var[0]:
        return False 
    if dupli[0][i+1]!=-1 and dupli[0][i+1]!=var[1]:
        return False 
    if dupli[1][i]!=-1 and dupli[1][i]!=var[2]:
        return False 
    if dupli[1][i+1]!=-1 and dupli[1][i+1]!=var[3]:
        return False 
    return True 


def dfs(org,dupli,i,old_d,new_d):
  
    n,m=len(org),1
    if org[i]==1:
        s=one
    else:
        s=zero

    for var in s:
        if check(var,i,dupli):
         
            save=[dupli[0][i],dupli[0][i+1],dupli[1][i],dupli[1][i+1]]
            change(dupli, var,i)
        
            if i<n-1:
                dfs(org,dupli,i+1,old_d,new_d)

            else:
                temp1=tuple(dupli[-1])
                if len(old_d)==0:
                  
                    if temp1 in new_d:
                        new_d[temp1]+=1
                    else:
                        new_d[temp1]=1
                   
                else:
                    temp2=tuple(dupli[0])
                    if temp2 in old_d:
                        if temp1 in new_d:
                            new_d[temp1]+=old_d[temp2]
                        else:
                            new_d[temp1]=old_d[temp2]
          
            dupli[0][i],dupli[0][i+1],dupli[1][i],dupli[1][i+1]=save[0],save[1],save[2],save[3]


def solution(g): 

    l=zip(*g) 
    g=[list(i) for i in l]  
    old_d = {}
    for L in g:
        
        dupli=[[-1]*(len(L)+1) for i in range(2)]
        new_d={}
        dfs(L, dupli, 0, old_d, new_d)
      
        old_d=new_d.copy()

    
    return sum(old_d.values())
one = set(permutations([1,0,0,0], 4))
z2 = set(permutations([1,1,0,0], 4))
z3 =set(permutations([1,1,1,0], 4))
zero = z2.union(z3)
zero.add((1,1,1,1))
zero.add((0,0,0,0))
# print(solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]))
# print(solution([[True, False, True], [False, True, False], [True, False, True]]))
# print(solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]))
# L=[[0] for i in range(9)]
# print(solution([
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
#          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
#          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
#          0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#         [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
#          1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
#         [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
#          1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
#          0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
#     ]
# ))
# print(solution(L))