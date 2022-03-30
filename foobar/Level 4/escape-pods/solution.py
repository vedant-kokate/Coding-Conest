from collections import defaultdict,deque
INF = 10**18
def change_graph(entrances, exits, cap):
    for i in range(len(cap)):
        cap[i]+=[0,0]
    cap.append([0]*len(cap[0]))
    cap.append([0]*len(cap[0]))
    for e in entrances:
        s=sum(cap[e])
        cap[-2][e]=s
    for e in exits:
        s=sum(cap[e])
        cap[e][-1]=INF
def bfs(cap,F,level):
    
    n=len(cap)
    for i in range(n):
        level[i]=0
    level[n-2] = 1    
    q=deque()
    q.append(n-2)
    while q:
      
        v=q.popleft()
  
        for i in range(n):
            if cap[v][i]!=0 and level[i] == 0 and cap[v][i]-F[v][i]:
                level[i] = level[v] + 1
                q.append(i)
 
    return level[-1]!=0

def dfs(cap,F,level,v,flow_cap):
   
    n=len(cap)
    if v==n-1: return flow_cap

    temp_flow = flow_cap

    for i in range(n):
        if cap[v][i]!=0 and level[i]==level[v]+1 and cap[v][i]-F[v][i]>0:
            f=dfs(cap,F,level,i,min(temp_flow,cap[v][i]-F[v][i]))
            F[v][i]+=f
            F[i][v]-=f
            temp_flow-=f
    return flow_cap-temp_flow




def solution(entrances, exits, cap):
    change_graph(entrances, exits, cap)
    # print(len(cap),len(cap[0]))
    n=len(cap)
    level = [0]*len(cap)
    F = [[0]*n for i in range(n)]
    flow = 0
    while bfs(cap,F,level):
        
        # print(level,flow)
        flow += dfs(cap,F,level,n-2,INF)

    return flow
 

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))