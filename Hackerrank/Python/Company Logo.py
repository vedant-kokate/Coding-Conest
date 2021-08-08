from collections import Counter
s=Counter(input())
ans=[]
for key,val in s.items():
    ans.append((key,val))
ans.sort(key=lambda x:(-x[1],x[0]))
for i in range(3):
    print(ans[i][0],ans[i][1])
