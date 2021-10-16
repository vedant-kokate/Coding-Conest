import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    a = I()
    ind = a.count(1)
    eng = a.count(2)

    if ind > eng:
        print("INDIA")
    elif ind < eng:
        print('ENGLAND')
    else:
        print("DRAW")