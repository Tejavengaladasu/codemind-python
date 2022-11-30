n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    if i%2==0:
        e.append(i)
    
print(e[len(e)-1])        