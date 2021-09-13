import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().split()))

vowel=['A','E','I','O','U']

for _ in range(int(input())):
    s=input()
    count=defaultdict(int)
    for c in s:
        if c!="\n":
            count[c]+=1
    
    ans=10**8
    # print(count)

    for this_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        min_sum=0
        for key,val in count.items():
            if key!=this_char:
                if key in vowel and this_char in vowel:
                    min_sum+=2*val
                elif key not in vowel and this_char not in vowel:
                    min_sum+=2*val
                else:
                    min_sum+=val
            # print(this_char,key,min_sum)
        # print("here",this_char,min_sum)
        ans=min(min_sum,ans)
    print(f"Case #{_+1}: {ans}")
