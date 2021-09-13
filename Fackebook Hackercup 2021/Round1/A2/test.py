s=input().strip()
ans=0
# print(s)
count=1
ans=0
for i in range(len(s)):
	for j in range(i,len(s)):
		n=int(s[i:j+1])
		# print(count,s[i:j+1])
		n=n%9-1
		if n>0:
			ans+=1
		count+=1
print(ans)

# This code is contributed by divyeshrabadiya07
