n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for j in l:
    if j%2!=0:
        l1.append(j)
print(*l1)        