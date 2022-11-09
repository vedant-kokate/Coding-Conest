import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
a,b=I()
s=round(b/a,3)
print("%.3f" % s)
