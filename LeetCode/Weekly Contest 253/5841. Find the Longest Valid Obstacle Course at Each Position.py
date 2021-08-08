from bisect import bisect_left,bisect_right
a=list(map(int,input().split()))
tail = [a[0]]
ans=[1]
ans[0]=1
for i in range(1, len(a)):
    if a[i] >= tail[-1]:
        tail.append(a[i])
        ans.append(len(tail))
    else:
        val=bisect_right(tail, a[i])       
        tail[val] = a[i]
        ans.append(val+1)
    # print(tail,ans)

print(*ans)

 
 
