n=int(input())
l=list(map(int,input().split()))
em=0
os=0
for i in range(n):
    if i%2==0:
        em=em+l[i]
    else:
        os=os+l[i]
d=abs(em-os)
if d==0:
    print("YES")
else:
    print("NO")
        