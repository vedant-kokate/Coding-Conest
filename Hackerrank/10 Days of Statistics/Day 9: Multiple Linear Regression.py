import numpy as np
from sklearn.linear_model import LinearRegression


m, n = map(int, input().split())
xy = [list(map(float, input().split())) for _ in range(n)]
y = np.array([i.pop() for i in xy])
X = np.array(xy)

lm = LinearRegression()
lm.fit(X, y)


q = int(input())
for _ in range(q):
    Q=np.array(input().split(), float).reshape(1,-1)
    ans=float(lm.predict(Q))
    print(round(ans,2))
    # print(float(lm.predict([np.array(input().split(), float)])))