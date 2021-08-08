from statistics import mean, stdev
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))

x_mean=mean(x)
y_mean=mean(y)

ans=0
for i in range(n):
    ans+=(x[i]-x_mean)*(y[i]-y_mean)

ans/=n
stdv_x = (sum([(i - x_mean)**2 for i in x]) / n)**0.5
stdv_y = (sum([(i - y_mean)**2 for i in y]) / n)**0.5

ans/=stdv_x
ans/=stdv_y

print(round(ans,3))