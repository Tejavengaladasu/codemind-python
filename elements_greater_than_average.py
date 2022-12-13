n=int(input())
l=list(map(int,input().split()))
c=0
d=sum(l)//n
for i in l:
    if i>=d:
        c+=1
print(c)        