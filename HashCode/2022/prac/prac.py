from collections import defaultdict
from fractions import Fraction as frac
from sys import stdin
input = stdin.readline

def score_count(ing_list):
    score=0
    for i in range(c):
        flag=True
        for l in p[i]['like']:
            if l not in ing_list:
                flag=False
                break
        for l in p[i]['dislike']:
            if l in ing_list:
                flag=False
                break
        if flag:
            score+=1
    return score


f_input = open('d_difficult.in.txt','r')
c=int(f_input.readline())
p=defaultdict(dict)
ing=defaultdict(dict)
for i in range(c):
    n,*l=f_input.readline().split()
    n=int(n)
    p[i]['like'] = l
    for indi_ing in l:
        if 'like' in ing[indi_ing]:
            ing[indi_ing]['like'].append(i)
        else:
            ing[indi_ing]['like'] = [i]

    n2,*l=f_input.readline().split()
    n2=int(n2)
    p[i]['dislike'] = l

    for indi_ing in l:
        if 'dislike' in ing[indi_ing]:
            ing[indi_ing]['dislike'].append(i)
        else:
            ing[indi_ing]['dislike'] = [i]

    p[i]['val'] = frac(1,(n+n2))

# print(p)
# print(ing,len(ing))
ingrediants=[]
for key in ing.keys():
    ing[key]['val'] = 0

    if 'like' in ing[key]:
        for pl in ing[key]['like']:
            ing[key]['val']+=p[pl]['val']
    
    if 'dislike' in ing[key]:
        for pl in ing[key]['dislike']:
            ing[key]['val']-=p[pl]['val']
    ingrediants.append((ing[key]['val'],key))

ingrediants.sort(reverse=True)

print(len(ingrediants))
# print(ingrediants)
max_score=-1

# lw=0
# h=len(ingrediants)
# ing_only=[]
# for v,i in ingrediants:
#     ing_only.append(i)
# # print('staring',lw,h)
# for _ in range(50):

#     mid=(lw+h)//2
#     mid2=(mid+h)//2
#     # print(mid)
#     s1=score_count(ing_only[:mid])
#     s2=score_count(ing_only[:mid2])
#     print(mid,mid2,s1,s2)
#     if s2>=s1:
#         lw=mid
#         if s2>max_score:
#             max_score=s2
#             f=open('outputb.txt','w')
#             f.write(str(len(ing_only[:mid2]))+" ")
#             for l in ing_only[:mid2]:
#                 # print(l)
#                 f.write(l+" ")
#             f.close()
#             print(s2)
#     else:
#         h=mid2
#         if s1>max_score:
#             max_score=s1
#             f=open('outputb.txt','w')
#             f.write(str(len(ing_only[:mid]))+" ")
#             for l in ing_only[:mid]:
#                 f.write(str(l)+" ")
#             f.close()
#             print(s1)
ing_list=set()
count=0
for val,key in ingrediants:
    ing_list.add(key)
    temp=score_count(ing_list)
    # if temp<max_score:
    #     break
    if temp>max_score:
        max_score=temp
        f=open('outputd.txt','w')
        f.write(str(len(ing_list))+" ")
        for l in ing_list:
            f.write(l+" ")
        f.close()
        # print(count,temp)
    count+=1








