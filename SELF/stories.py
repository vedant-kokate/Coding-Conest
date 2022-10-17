import pandas as pd
import numpy as np
# import os
df = pd.read_csv('./out.csv')
def f(diff,score):
    # diff = int(input())
    a=diff/400
    b=10**a
    c=b+1
    d=1/c
    e=100*(score-d)
    return e

from random import randint as r
n=len(df)
print(df.head())
for _ in range(100): 
  a,b=r(0,n-1),r(0,n-1)
  print(df.loc[a])
  print("------------------")
  print(df.loc[b])
  score=float(input())
  diff=df.at[b,'Rating']-df.at[a,'Rating']
  change=f(diff,score)
  df.at[a,'Rating'] += change 
  df.at[b,'Rating'] -= change
  print(df.at[a,'Rating'],df.at[b,'Rating'])
#   os.system('cls')
df.to_csv('out.csv')