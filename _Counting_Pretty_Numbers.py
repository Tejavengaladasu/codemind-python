x=int(input())

for i in range(x):
    m,n=map(int,input().split())
    c=0
    for j in range(m,n+1):
        d=0
        d=j%10
        if d==2 or d==3 or d==9:
            c+=1
    print(c)        
        
    