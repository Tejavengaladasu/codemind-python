n=int(input())
l=list(map(int,input().split()))
p=0
for i in range(n):
    if l[i]%2==0:
        p=i
print(p)    
        
        