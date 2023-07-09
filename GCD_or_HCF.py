n,m=map(int,input().split())
l1=[]
l2=[]
l=[]
for i in range(1,n+1):
    if n%i==0:
        l1.append(i)
for i in range(1,m+1):
    if m%i==0:
        l2.append(i)
for i in l1:
    if i in l2:
        l.append(i)
print(max(l))