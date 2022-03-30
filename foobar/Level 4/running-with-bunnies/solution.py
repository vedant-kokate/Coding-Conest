from itertools import permutations
def solution(times, times_limit): 

    def score(way):
        res = 0
        for i in range(1,len(way)):
            res+=times[way[i-1]+1][way[i]+1]
        res+=times[0][way[0]+1]
        res+=times[way[-1]+1][-1]
        return res

    n=len(times)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                times[i][j] = min(times[i][j],times[i][k]+times[k][j])
    for i in range(n):
        if times[i][i]<0:
            return list(range(n-2))
    
    tot_way=[]
    for p in range(1,n-1):
        for way in list(permutations(range(n-2),p)):
            sc =score(way)
            if sc<=times_limit:
                if len(tot_way)==0:
                    tot_way.append(way)
                else:
                    if len(way)>len(tot_way[0]):
                        tot_way=[]
                        tot_way.append(way)
                    elif len(way)==len(tot_way[0]):
                        tot_way.append(way)
            # print(way,sc,tot_way)
    tot_way.sort()
    # print(tot_way)
    if len(tot_way)==0:
        return []
    L = list(tot_way[0])
    L.sort()
    return L

# times = [list(map(int,input().split()))]
# for i in range(len(times[0])-1):
#     times.append(list(map(int,input().split())))
#     # print(times)
# times_limit = int(input())
# print(solution(times, times_limit))
m= [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]
print(solution(m,6))