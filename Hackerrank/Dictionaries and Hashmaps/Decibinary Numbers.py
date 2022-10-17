# # from collections import defaultdict,deque
# # a=list(range(1,11))
# # def convert(x):
# #     val=0
# #     num=1
# #     while x:
# #         rem=x%10
# #         x//=10
# #         val += rem*num
# #         num *=2
# #     return val
# # def f(x,y):
# #     x_val,y_val=0,0
# # def bfs(x):
# #     stack=deque()
# #     ans=set()
# #     stack=deque([str(x)])
# #     while stack:
# #         # print(stack)
# #         cur=stack.popleft()
# #         ans.add(cur)
# #         l=[]
# #         l[:]=cur
# #         for i in range(0,len(l)-1):
# #             if l[i]!='0' and (l[i+1]!='8' and l[i+1]!='9'):
# #                 # print(l)
# #                 l[i]=str(int(l[i])-1)
# #                 l[i+1]=str(int(l[i+1])+2)
# #                 temp=int("".join(l))
# #                 if temp not in ans:
# #                     stack.append(str(temp))
# #                 l[i]=str(int(l[i])+1)
# #                 l[i+1]=str(int(l[i+1])-2)
# #     # print(ans)
# #     return len(ans)
# from math import ceil
# a=[1,2,4,6,10]
# sum_=sum(a)
# i=6
# while sum_*2<10**16:
#     val=a[i-1-1]+a[ceil(i/2)-1] - a[ceil((i-5)/2)-1]
#     sum_+=val
#     a.append(val)
#     i+=1
# print(sum_,i,i*2,max(a))
# # d=defaultdict(list)

# # for i in range(1,30):
# #     if i%2==0:
# #         print(i,bfs(bin(i)[2:]))
# # print(bfs(bin(19)[2:]))
# # for key in d.keys():
# #     if key<20:
# #         print(key,len(d[key]))


ans =[]

def gen(d, s, v):
    print(d,s,v)
    if s < 0 or s > 9*((1 << (d+1))-1):
        pass
    elif (s == 0 and d == -1):
        ans.append(v)
    else:	
        for i in range(10):
            gen(d-1, s-i*(1 << d), v*10+i)
	


# main()
val=0
gen(20,10,0)
print(ans)
print(len(ans))
# 	val = 0, cur, q, x;
# 	for (i = 0; i < 600; i++)
# 		gen(20, i, 0);
# 	cin >> q;
# 	while (q--)
	
# 		cin >> x;
# 		cout << ans[x-1] << '\n';
	
