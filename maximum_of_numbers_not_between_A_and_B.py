n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
c=0
for i in l:
    if i<a or i>b:
        s.append(i)
        c+=1
if c<1:
    print(-1)
else:
    print(max(s))