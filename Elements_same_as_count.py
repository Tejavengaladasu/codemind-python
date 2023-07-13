n=int(input())
l=list(map(int,input().split()))
d={}
l1=[]
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if i==j:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    print(*l1)