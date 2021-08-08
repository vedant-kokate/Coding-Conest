s=input()
pos=[]
for i,val in enumerate(s):
    if val=='[':
        pos.append(i)

# print(pos)

count=0
ans=0
for i,val in enumerate(s):
    if val=='[':
        count+=1
    else:
        count-=1
    if count<0:
        ans+=1
        target=pos.pop()
        # s[target]=']'
        # s[i]='['
        count+=2
print(ans)