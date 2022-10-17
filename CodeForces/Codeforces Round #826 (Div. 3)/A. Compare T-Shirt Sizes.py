import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

s={'S':0,'M':1,'L':2}
for _ in range(int(input())):
    a,b=input().split()
    # print(a[-1],b[-1])
    if a==b:
        print('=')
    elif(a[-1]==b[-1]):
        if a[-1]=='S':
            if len(a)>len(b):
                print("<")
            else:
                print(">")
        else:
            if len(a)>len(b):
                print(">")
            else:
                print("<")
    elif s[a[-1]]>s[b[-1]]:
        print(">")
    else:
        print("<")
