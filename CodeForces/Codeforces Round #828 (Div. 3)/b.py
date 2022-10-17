import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n, q = I()
    a=I()
    odd_sum = 0
    odd_l = 0
    even_sum = 0
    even_l = 0
    for i in a:
        if i%2:
            odd_sum += i 
            odd_l += 1
        else:
            even_l +=1
            even_sum += i 
    
    for Q in range(q):
        t,x=I()
        if t==0:
            even_sum += even_l*x
            if x%2:                
                odd_sum += even_sum
                even_sum = 0
                even_l = 0
                odd_l = n
    
        else:
            odd_sum += odd_l*x
            if x%2==1:
                even_sum += odd_sum
                odd_sum = 0
                odd_l = 0
                even_l = n
        print(even_sum+odd_sum)