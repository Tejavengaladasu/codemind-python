n=input()
l=list(n)
for i in l:
    if i==",":
        l.remove(i)
l1=[]
for i in l:
    sum=0
    for j in range(1,int(i)+1):
        if int(i)%j==0:
            sum+=j
    if str(sum) in l:
        l1.append(i)
l1.sort()
if len(l1)==0:
    print(-1)
else:
    print(*l1)
            