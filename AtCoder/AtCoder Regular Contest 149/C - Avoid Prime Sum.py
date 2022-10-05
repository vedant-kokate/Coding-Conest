import sys
input = sys.stdin.readline
import math
def I():return list(map(int,input().split()))
def p(q):
    for i in range(n):
        for j in range(n):
            print(q.pop(),end=" ")
        print()
 
n=int(input())
if n == 3:
	print(5,1,3)
	print(4,8,6)
	print(2,7,9)
	exit()
 
if n == 4:
	print(15,11,16,12)
	print(13,3,6,9)
	print(14,7,8,1)
	print(4,2,10,5)
	exit()
 
if n == 5:
	print(1,3,5,7,9)
	print(11,19,15,13,17)
	print(21,23,25,2,4)
	print(6,10,8,12,14)
	print(16,18,20,22,24)
	exit()
    
a,b,c,d=[],[],[],[]
for i in range(1,n*n+1):
    if i%2:
        if i%3:
            a.append(i)
        else:
            b.append(i)
    else:
        if i%3==0:
            c.append(i)
        else:
            d.append(i)
q=a+b+c+d
p(q)