n=int(input())
l=list(map(int,input().split()))
m,z=map(int,input().split())
a=[]
b=[]
for i in l:
    if i>=m and i<=z:
        a.append(i)
    else:
        b.append(i)
print(sum(b))        
        