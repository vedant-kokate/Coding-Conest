# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
k=input()
pattern = re.compile(k)
r = pattern.search(s)
if r==None:
    print(f"({-1}, {-1})")
while r:
    print (f"({r.start()}, {r.end()-1})")
    r = pattern.search(s,r.start() + 1)