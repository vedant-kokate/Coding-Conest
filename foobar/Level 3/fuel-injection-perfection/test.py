from heapq import heapify,heappop,heappush
heap=[(0,1)]
heapify(heap)
lim=10**5
ans1=[-1]*lim

while heap:
    dis,val = heappop(heap)   
    if ans1[val]!=-1:continue 

    ans1[val] = dis
    if val+1<lim and ans1[val+1]==-1:
        heappush(heap, (dis+1,val+1))
    if val*2<lim and ans1[val*2]==-1:
        heappush(heap, (dis+1,val*2))
    if val-1>0 and ans1[val-1]==-1:
        heappush(heap, (dis+1,val-1))

# print(ans1[:100])
def val(n):
        temp = "{0:b}".format(int(n))
        return temp.count('1')*2+temp.count('0')
print('first part')
for n in range(1,lim):
    ans=0
    N=n
    while N>1:
        if N%2:
            if val(N-1)<val(N+1):
                N-=1
                ans+=1
            else:
                N+=1
                ans+=1
        else:
            N//=2
            ans+=1
    if ans!=ans1[n]:
        print(n,ans,ans1[n])
