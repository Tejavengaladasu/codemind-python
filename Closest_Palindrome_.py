n=int(input())
l=[]
l1=[]
for i in range(1,n):
    s=str(i)
    a=s[::-1]
    if s==a:
        l.append(i)
for j in range(n+1,n*n):
    s1=str(j)
    a1=s1[::-1]
    if s1==a1:
        l1.append(j)
m=max(l)
m1=min(l1)
e=(n-m)
q=(m1-n)
if e==q:
    print(m,m1)
elif e>q:
    print(m1)
else:
    print(m)