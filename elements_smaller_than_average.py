n=int(input())
l=list(map(int,input().split()))
d=sum(l)//n
c=0
for i in l:
    if i<=d:
        c+=1
print(c)        