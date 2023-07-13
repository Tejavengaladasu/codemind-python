n=int(input())
l=list(map(int,input().split()))
d={}
c=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if i==j:
        c+=1
print(c)