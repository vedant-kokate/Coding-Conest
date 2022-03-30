def solution(start, length):
    def xor_range(l,r):
        def xor(n):
            if n%4==0: return n
            if n%4==1: return 1
            if n%4==2: return n+1
            return 0
        return xor(l-1)^xor(r)
    ans = 0
    for L in range(length-1,-1,-1):
        ans = ans^xor_range(start,start+L)
        start+=length
    return ans
    # Your code here
start,length = map(int,input().split())
print(solution(start, length))