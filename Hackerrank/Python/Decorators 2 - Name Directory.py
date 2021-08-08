import operator

def person_lister(f):
    def inner(people):
        people.sort(key = lambda x:int(x[2]))
        ans=[]
        for fn,ln,age,g in people:
            s=""
            if g=='M':
                s="Mr. "
            else:
                s="Ms. "
            s+=fn+" "+ln
            ans.append(s)
        # print(people)
        return ans
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')