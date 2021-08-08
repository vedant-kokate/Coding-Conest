
from fractions import Fraction as frac
def findWays(f, d, s):
    mem = [[frac(0,1) for i in range(s+1)] for j in range(d+1)]
    mem[0][0] = frac(1,1)
    for i in range(1, d+1):
        for j in range(1, s+1):
            mem[i][j] = mem[i][j - 1] + mem[i - 1][j - 1]
            if j - f - 1 >= 0:
                mem[i][j] -= mem[i - 1][j - f - 1]
    return mem[d]


dice_face=6
num_of_dice=2
ans=findWays(dice_face, num_of_dice, num_of_dice*dice_face)
# print(ans)
for i in range(1,len(ans)):
    ans[i]+=ans[i-1]
# print(ans)

for i in range(1,len(ans)):
    ans[i]/=36
print(ans[9])

