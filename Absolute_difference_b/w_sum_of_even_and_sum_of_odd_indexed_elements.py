n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(n):
    if i%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
print(abs(sum(e)-sum(o)))        